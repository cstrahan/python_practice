import pytest

# Given an int n, return the absolute difference between n and 21, except return
# double the absolute difference if n is over 21.
def diff21(n):
    pass


@pytest.mark.parametrize(
    "n,expected",
    [
        (19, 2),
        (10, 11),
        (21, 0),
        (22, 2),
        (25, 8),
        (30, 18),
        (0, 21),
        (1, 20),
        (2, 19),
        (-1, 22),
        (-2, 23),
        (50, 58),
    ],
)
def test_diff21(n, expected):
    assert diff21(n) == expected
