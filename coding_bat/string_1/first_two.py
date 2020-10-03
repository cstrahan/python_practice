import pytest

# Given a string, return the string made of its first two chars, so the String
# "Hello" yields "He". If the string is shorter than length 2, return whatever
# there is, so "X" yields "X", and the empty string "" yields the empty string
# "".
def first_two(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "He"),
        ("abcdefg", "ab"),
        ("ab", "ab"),
        ("a", "a"),
        ("", ""),
        ("Kitten", "Ki"),
        ("hi", "hi"),
        ("hiya", "hi"),
    ],
)
def test_first_two(str, expected):
    assert first_two(str) == expected
