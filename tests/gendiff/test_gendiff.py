from gendiff.gendiff import generate_diff

from tests.fixtures.expected_strings import NESTED_PLAIN_DIFF_STR_12
from tests.fixtures.expected_strings import NESTED_STYLISH_DIFF_STR_12


def test_gendiff_stylish_nested():
    assert generate_diff(
        './tests/fixtures/nested1.json',
        './tests/fixtures/nested2.json',
        'stylish',
    ) == NESTED_STYLISH_DIFF_STR_12
    assert generate_diff(
        './tests/fixtures/nested1.yaml',
        './tests/fixtures/nested2.yaml',
        'stylish',
    ) == NESTED_STYLISH_DIFF_STR_12
    assert generate_diff(
        './tests/fixtures/nested1.json',
        './tests/fixtures/nested2.yaml',
        'stylish',
    ) == NESTED_STYLISH_DIFF_STR_12
    assert generate_diff(
        './tests/fixtures/nested1.yaml',
        './tests/fixtures/nested2.json',
        'stylish',
    ) == NESTED_STYLISH_DIFF_STR_12


def test_gendiff_plain_nested():
    assert generate_diff(
        './tests/fixtures/nested1.json',
        './tests/fixtures/nested2.json',
        'plain',
    ) == NESTED_PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/nested1.yaml',
        './tests/fixtures/nested2.yaml',
        'plain',
    ) == NESTED_PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/nested1.json',
        './tests/fixtures/nested2.yaml',
        'plain',
    ) == NESTED_PLAIN_DIFF_STR_12

    assert generate_diff(
        './tests/fixtures/nested1.yaml',
        './tests/fixtures/nested2.json',
        'plain',
    ) == NESTED_PLAIN_DIFF_STR_12
