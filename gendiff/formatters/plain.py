def _stringify(data):
    if isinstance(data, dict):
        return '[complex value]'
    special_values = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }
    str_value = str(data)
    if isinstance(data, str):
        str_value = f"'{str_value}'"
    return special_values.get(str_value, str_value)


def _upd_path(path, new_token):
    return new_token if path == '' else f'{path}.{new_token}'


def gen_plain_diff(dicts_diff: dict) -> str:    # noqa: C901
    """
     Возвращает специальным образом отформатированное "простое"
     текстовое представление данного dicts diff файла.

    Аргументы:
        dicts_diff: Словарь специального формата, описывающий
        разницу между двумя словарями

    Возвращает:
        Специально отформатированное "простое" текстовое
        представление dicts_diff.
    """

    lines = []

    def helper(dict_value, path):

        for key in sorted(dict_value):
            key_path = _upd_path(path, key)
            value = dict_value[key]
            if isinstance(value, dict):
                helper(value, key_path)
                continue

            status, content = value
            if status == 'unchanged':
                continue
            line = f"Property '{key_path}' was "
            if status == 'changed':
                old_content, new_content = content
                value_str_old = _stringify(old_content)
                value_str_new = _stringify(new_content)
                line += f'updated. From {value_str_old} to {value_str_new}'
            elif status == 'added':
                line += f'added with value: {_stringify(content)}'
            elif status == 'deleted':
                line += 'removed'

            lines.append(line)

    helper(dicts_diff, '')
    return '\n'.join(lines)
