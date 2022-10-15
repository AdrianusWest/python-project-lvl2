from gendiff.formatters import gen_json_diff, gen_plain_diff, gen_stylish_diff


def formatting(tree: dict, format_name: str):
    if format_name == 'plain':
        return gen_plain_diff(tree)
    if format_name == 'stylish':
        return gen_stylish_diff(tree)
    if format_name == 'json':
        return gen_json_diff(tree)
    raise ValueError(f'Unknown format: {format_name}!')
