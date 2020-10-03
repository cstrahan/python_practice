import pytest

# The number 6 is a truly great number. Given two int values, a and b, return
# True if either one is 6. Or if their sum or difference is 6. Note: the
# function abs(num) computes the absolute value of a number.
def love6(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 4, True),
        (4, 5, False),
        (1, 5, True),
        (1, 6, True),
        (1, 8, False),
        (1, 7, True),
        (7, 5, False),
        (8, 2, True),
        (6, 6, True),
        (-6, 2, False),
        (-4, -10, True),
        (-7, 1, False),
        (7, -1, True),
        (-6, 12, True),
        (-2, -4, False),
        (7, 1, True),
        (0, 9, False),
        (8, 3, False),
        (3, 3, True),
        (3, 4, False),
    ],
)
def test_love6(a, b, expected):
    assert love6(a, b) == expected
