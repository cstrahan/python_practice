import pytest

# Given 3 int values, a b c, return their sum. However, if one of the values is
# 13 then it does not count towards the sum and values to its right do not
# count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (1, 2, 13, 3),
        (1, 13, 3, 1),
        (1, 13, 13, 1),
        (6, 5, 2, 13),
        (13, 2, 3, 0),
        (13, 2, 13, 0),
        (13, 13, 2, 0),
        (9, 4, 13, 13),
        (8, 13, 2, 8),
        (7, 2, 1, 10),
        (3, 3, 13, 6),
    ],
)
def test_lucky_sum(a, b, c, expected):
    assert lucky_sum(a, b, c) == expected
