def set_dict_value(d: dict, path: tuple, value):
    """
    В заданном словаре изменяет (или добавляет) значение в указанном
    пути. Функция изменяет словарь.
    """
    if len(path) != 0:
        current = d
        for key in path[:-1]:
            if key not in current or type(current[key]) != dict:
                current[key] = {}
            current = current[key]
        current[path[-1]] = value


def build_ast(dict_old: dict, dict_new: dict) -> dict:  # noqa: C901
    """
    AST - специальный формат дифф-словаря, который описывает,
    что произошло с каждым ключом в сравниваемых словарях:
    был ли он добавлен, изменен или удален, а также соответствующие
    значения словаря.
    """
    diff_dict = {}

    def helper(old_dict, new_dict, path):

        old_keys = old_dict.keys()
        new_keys = new_dict.keys()

        added_keys = new_keys - old_keys
        deleted_keys = old_keys - new_keys
        common_keys = new_keys & old_keys

        for key in added_keys:
            set_dict_value(diff_dict, path + (key,),
                           ('added', new_dict[key]))

        for key in deleted_keys:
            set_dict_value(diff_dict, path + (key,),
                           ('deleted', old_dict[key]))

        for key in common_keys:
            value_new = new_dict[key]
            value_old = old_dict[key]

            if type(value_new) == type(value_old) == dict:
                helper(value_old, value_new, path + (key,))
            elif value_new != value_old:
                set_dict_value(diff_dict, path + (key,),
                               ('changed', (value_old, value_new)))
            else:
                set_dict_value(diff_dict, path + (key,),
                               ('unchanged', value_old))

    helper(dict_old, dict_new, tuple())
    return diff_dict
