import pytest

# Given 2 ints, a and b, return their sum. However, sums in the range 10..19
# inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 7),
        (9, 4, 20),
        (10, 11, 21),
        (12, -3, 9),
        (-3, 12, 9),
        (4, 5, 9),
        (4, 6, 20),
        (14, 7, 21),
        (14, 6, 20),
    ],
)
def test_sorta_sum(a, b, expected):
    assert sorta_sum(a, b) == expected
