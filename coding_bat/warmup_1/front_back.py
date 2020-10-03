import pytest

# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("code", "eodc"),
        ("a", "a"),
        ("ab", "ba"),
        ("abc", "cba"),
        ("", ""),
        ("Chocolate", "ehocolatC"),
        ("aavJ", "Java"),
        ("hello", "oellh"),
    ],
)
def test_front_back(str, expected):
    assert front_back(str) == expected
