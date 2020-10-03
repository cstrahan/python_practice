import pytest

# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.
def sum_double(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (3, 2, 5),
        (2, 2, 8),
        (-1, 0, -1),
        (3, 3, 12),
        (0, 0, 0),
        (0, 1, 1),
        (3, 4, 7),
    ],
)
def test_sum_double(a, b, expected):
    assert sum_double(a, b) == expected
