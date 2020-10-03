import pytest

# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return a
# new string which is 3 copies of the front.
def front3(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Java", "JavJavJav"),
        ("Chocolate", "ChoChoCho"),
        ("abc", "abcabcabc"),
        ("abcXYZ", "abcabcabc"),
        ("ab", "ababab"),
        ("a", "aaa"),
        ("", ""),
    ],
)
def test_front3(str, expected):
    assert front3(str) == expected
