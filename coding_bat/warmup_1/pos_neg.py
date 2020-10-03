import pytest

# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are
# negative.
def pos_neg(a, b, negative):
    pass


@pytest.mark.parametrize(
    "a,b,negative,expected",
    [
        (1, -1, False, True),
        (-1, 1, False, True),
        (-4, -5, True, True),
        (-4, -5, False, False),
        (-4, 5, False, True),
        (-4, 5, True, False),
        (1, 1, False, False),
        (-1, -1, False, False),
        (1, -1, True, False),
        (-1, 1, True, False),
        (1, 1, True, False),
        (-1, -1, True, True),
        (5, -5, False, True),
        (-6, 6, False, True),
        (-5, -6, False, False),
        (-2, -1, False, False),
        (1, 2, False, False),
        (-5, 6, True, False),
        (-5, -5, True, True),
    ],
)
def test_pos_neg(a, b, negative, expected):
    assert pos_neg(a, b, negative) == expected
