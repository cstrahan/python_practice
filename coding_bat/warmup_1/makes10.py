import pytest

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (9, 10, True),
        (9, 9, False),
        (1, 9, True),
        (10, 1, True),
        (10, 10, True),
        (8, 2, True),
        (8, 3, False),
        (10, 42, True),
        (12, -2, True),
    ],
)
def test_makes10(a, b, expected):
    assert makes10(a, b) == expected
