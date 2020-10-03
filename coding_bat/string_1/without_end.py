import pytest

# Given a string, return a version without the first and last char, so "Hello"
# yields "ell". The string length will be at least 2.
def without_end(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "ell"),
        ("java", "av"),
        ("coding", "odin"),
        ("code", "od"),
        ("ab", ""),
        ("Chocolate!", "hocolate"),
        ("kitten", "itte"),
        ("woohoo", "ooho"),
    ],
)
def test_without_end(str, expected):
    assert without_end(str) == expected
