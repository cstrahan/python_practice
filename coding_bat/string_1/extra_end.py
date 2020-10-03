import pytest

# Given a string, return a new string made of 3 copies of the last 2 chars of
# the original string. The string length will be at least 2.
def extra_end(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "lololo"),
        ("ab", "ababab"),
        ("Hi", "HiHiHi"),
        ("Candy", "dydydy"),
        ("Code", "dedede"),
    ],
)
def test_extra_end(str, expected):
    assert extra_end(str) == expected
