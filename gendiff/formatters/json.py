import json


def gen_json_diff(dicts_diff: dict) -> str:
    """
    Возвращает json-представление данного файла dicts diff
    (внутренней структуры)

    Аргументы:
        dicts_diff: Словарь специального формата, который
        описывает разницу между двумя словарями

    Возвращает:
        json-представление внутренней структуры dicts_diff.
    """
    return json.dumps(dicts_diff, indent=2)
