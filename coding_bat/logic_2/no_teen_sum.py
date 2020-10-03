import pytest

# Given 3 int values, a b c, return their sum. However, if any of the values is
# a teen -- in the range 13..19 inclusive -- then that value counts as 0, except
# 15 and 16 do not count as a teens. Write a separate helper "def
# fix_teen(n):"that takes in an int value and returns that value fixed for the
# teen rule. In this way, you avoid repeating the teen code 3 times (i.e.
# "decomposition"). Define the helper below and at the same indent level as the
# main no_teen_sum().
def no_teen_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (2, 13, 1, 3),
        (2, 1, 14, 3),
        (2, 1, 15, 18),
        (2, 1, 16, 19),
        (2, 1, 17, 3),
        (17, 1, 2, 3),
        (2, 15, 2, 19),
        (16, 17, 18, 16),
        (17, 18, 19, 0),
        (15, 16, 1, 32),
        (15, 15, 19, 30),
        (15, 19, 16, 31),
        (5, 17, 18, 5),
        (17, 18, 16, 16),
        (17, 19, 18, 0),
    ],
)
def test_no_teen_sum(a, b, c, expected):
    assert no_teen_sum(a, b, c) == expected
