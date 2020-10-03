import pytest

# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
    pass


@pytest.mark.parametrize(
    "weekday,vacation,expected",
    [
        (False, False, True),
        (True, False, False),
        (False, True, True),
        (True, True, True),
    ],
)
def test_sleep_in(weekday, vacation, expected):
    assert sleep_in(weekday, vacation) == expected
