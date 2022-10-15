import json
import pathlib

import yaml


def get_file_extension(file_path: str) -> str:
    return pathlib.Path(file_path).suffix


def parse(data, extension: str) -> dict:
    if extension == 'json':
        return json.load(data)
    if extension == 'yaml':
        return yaml.safe_load(data)
    if extension == 'yml':
        return yaml.safe_load(data)

    raise ValueError(f'Unknown extension:{extension}!')


def get_data(file_path: str) -> dict:
    """Парсинг указанного JSON/YAML файла в словарь.

    Args:
        file_path: путь к JSON/YAML
    возвращает:
        словарь-представление данного файла

    """
    extension = get_file_extension(file_path)
    with open(file_path) as data:
        return parse(data, extension)
