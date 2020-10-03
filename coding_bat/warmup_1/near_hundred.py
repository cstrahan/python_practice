import pytest

# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
# computes the absolute value of a number.
def near_hundred(n):
    pass


@pytest.mark.parametrize(
    "n,expected",
    [
        (93, True),
        (90, True),
        (89, False),
        (110, True),
        (111, False),
        (121, False),
        (-101, False),
        (-209, False),
        (190, True),
        (209, True),
        (0, False),
        (5, False),
        (-50, False),
        (191, True),
        (189, False),
        (200, True),
        (210, True),
        (211, False),
        (290, False),
    ],
)
def test_near_hundred(n, expected):
    assert near_hundred(n) == expected
