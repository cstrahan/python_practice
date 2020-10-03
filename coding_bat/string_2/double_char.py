import pytest

# Given a string, return a string where for every char in the original, there
# are two chars.
def double_char(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("The", "TThhee"),
        ("AAbb", "AAAAbbbb"),
        ("Hi-There", "HHii--TThheerree"),
        ("Word!", "WWoorrdd!!"),
        ("!!", "!!!!"),
        ("", ""),
        ("a", "aa"),
        (".", ".."),
        ("aa", "aaaa"),
    ],
)
def test_double_char(str, expected):
    assert double_char(str) == expected
