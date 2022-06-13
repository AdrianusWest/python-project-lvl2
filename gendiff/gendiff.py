from gendiff.ast_builder import build_ast
from gendiff.input_parser import parse_datafile
from gendiff.formatters import gen_plain_diff, gen_stylish_diff, gen_json_diff


def generate_diff(
        file_path1: str, file_path2: str, format_name='stylish') -> str:
    """
    Возвращает заданный специальным образом отформатированный
    ('plain'/'stylish'/'json') текст-представление разницы между
    двумя JSON или YAML.

    Args:
        file_path1: Путь к исходному JSON/YAML,
        file_path2: Путь к конечному JSON/YAML,
        format_name: имя формата текстового представления (по
        умолчанию 'stylish').
    Возвращает:
        заданное специальное форматированное текстовое
        представление разницы между заданными файлами
    """
    dict1 = parse_datafile(file_path1)
    dict2 = parse_datafile(file_path2)

    return {'plain': gen_plain_diff,
            'stylish': gen_stylish_diff,
            'json': gen_json_diff,
            }[format_name](build_ast(dict1, dict2))
