import pytest

# Given a string and a non-negative int n, return a larger string that is n
# copies of the original string.
def string_times(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("Hi", 2, "HiHi"),
        ("Hi", 3, "HiHiHi"),
        ("Hi", 1, "Hi"),
        ("Hi", 0, ""),
        ("Hi", 5, "HiHiHiHiHi"),
        ("Oh Boy!", 2, "Oh Boy!Oh Boy!"),
        ("x", 4, "xxxx"),
        ("", 4, ""),
        ("code", 2, "codecode"),
        ("code", 3, "codecodecode"),
    ],
)
def test_string_times(str, n, expected):
    assert string_times(str, n) == expected
