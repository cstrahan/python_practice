import pytest

# Given a non-negative number "num", return True if num is within 2 of a
# multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5)
# is 2. See also: Introduction to Mod
def near_ten(num):
    pass


@pytest.mark.parametrize(
    "num,expected",
    [
        (12, True),
        (17, False),
        (19, True),
        (31, True),
        (6, False),
        (10, True),
        (11, True),
        (21, True),
        (22, True),
        (23, False),
        (54, False),
        (155, False),
        (158, True),
        (3, False),
        (1, True),
    ],
)
def test_near_ten(num, expected):
    assert near_ten(num) == expected
