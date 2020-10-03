import pytest

# Given a non-empty string and an int n, return a new string where the char at
# index n has been removed. The value of n will be a valid index of a char in
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("kitten", 1, "ktten"),
        ("kitten", 0, "itten"),
        ("kitten", 4, "kittn"),
        ("Hi", 0, "i"),
        ("Hi", 1, "H"),
        ("code", 0, "ode"),
        ("code", 1, "cde"),
        ("code", 2, "coe"),
        ("code", 3, "cod"),
        ("chocolate", 8, "chocolat"),
    ],
)
def test_missing_char(str, n, expected):
    assert missing_char(str, n) == expected
