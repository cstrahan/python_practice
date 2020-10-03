import pytest

# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is
# less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
    pass


@pytest.mark.parametrize(
    "n,outside_mode,expected",
    [
        (5, False, True),
        (11, False, False),
        (11, True, True),
        (10, False, True),
        (10, True, True),
        (9, False, True),
        (9, True, False),
        (1, False, True),
        (1, True, True),
        (0, False, False),
        (0, True, True),
        (-1, False, False),
        (-1, True, True),
        (99, False, False),
        (-99, True, True),
    ],
)
def test_in1to10(n, outside_mode, expected):
    assert in1to10(n, outside_mode) == expected
