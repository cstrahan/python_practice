import pytest

# Given 2 strings, a and b, return the number of the positions where they
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
# the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("xxcaazz", "xxbaaz", 3),
        ("abc", "abc", 2),
        ("abc", "axc", 0),
        ("hello", "he", 1),
        ("he", "hello", 1),
        ("h", "hello", 0),
        ("", "hello", 0),
        ("aabbccdd", "abbbxxd", 1),
        ("aaxxaaxx", "iaxxai", 3),
        ("iaxxai", "aaxxaaxx", 3),
    ],
)
def test_string_match(a, b, expected):
    assert string_match(a, b) == expected
