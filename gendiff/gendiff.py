from gendiff.ast_builder import build_ast
from gendiff.formatter import formatting
from gendiff.parser import get_data


def generate_diff(file_path1: str, file_path2: str,
                  format_name='stylish') -> str:
    """Возвращает заданный специальным образом отформатированный
    ('plain'/'stylish'/'json') текст-представление разницы
    между двумя JSON или YAML.

    Args:
        file_path1: Путь к исходному JSON/YAML,
        file_path2: Путь к конечному JSON/YAML,
        format_name: имя формата текстового представления (по
        умолчанию 'stylish').

    Возвращает:
        заданное специальное форматированное текстовое
        представление разницы между заданными файлами.

    """
    dict1 = get_data(file_path1)
    dict2 = get_data(file_path2)
    ast = build_ast(dict1, dict2)
    return formatting(ast, format_name)
