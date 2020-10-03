import pytest

# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int
# value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and
# 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,
# your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    pass


@pytest.mark.parametrize(
    "speed,is_birthday,expected",
    [
        (60, False, 0),
        (65, False, 1),
        (65, True, 0),
        (80, False, 1),
        (85, False, 2),
        (85, True, 1),
        (70, False, 1),
        (75, False, 1),
        (75, True, 1),
        (40, False, 0),
        (40, True, 0),
        (90, False, 2),
    ],
)
def test_caught_speeding(speed, is_birthday, expected):
    assert caught_speeding(speed, is_birthday) == expected
