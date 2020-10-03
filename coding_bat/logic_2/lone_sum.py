import pytest

# Given 3 int values, a b c, return their sum. However, if one of the values is
# the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (3, 2, 3, 2),
        (3, 3, 3, 0),
        (9, 2, 2, 9),
        (2, 2, 9, 9),
        (2, 9, 2, 9),
        (2, 9, 3, 14),
        (4, 2, 3, 9),
        (1, 3, 1, 3),
    ],
)
def test_lone_sum(a, b, c, expected):
    assert lone_sum(a, b, c) == expected
