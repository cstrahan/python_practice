import pytest

# Given three ints, a b c, return True if one of b or c is "close" (differing
# from a by at most 1), while the other is "far", differing from both other
# values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 10, True),
        (1, 2, 3, False),
        (4, 1, 3, True),
        (4, 5, 3, False),
        (4, 3, 5, False),
        (-1, 10, 0, True),
        (0, -1, 10, True),
        (10, 10, 8, True),
        (10, 8, 9, False),
        (8, 9, 10, False),
        (8, 9, 7, False),
        (8, 6, 9, True),
    ],
)
def test_close_far(a, b, c, expected):
    assert close_far(a, b, c) == expected
