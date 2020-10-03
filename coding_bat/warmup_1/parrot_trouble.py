import pytest

# We have a loud talking parrot. The "hour" parameter is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking and the hour is
# before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    pass


@pytest.mark.parametrize(
    "talking,hour,expected",
    [
        (True, 6, True),
        (True, 7, False),
        (False, 6, False),
        (True, 21, True),
        (False, 21, False),
        (False, 20, False),
        (True, 23, True),
        (False, 23, False),
        (True, 20, False),
        (False, 12, False),
    ],
)
def test_parrot_trouble(talking, hour, expected):
    assert parrot_trouble(talking, hour) == expected
