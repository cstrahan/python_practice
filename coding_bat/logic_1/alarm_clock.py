import pytest

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
# boolean indicating if we are on vacation, return a string of the form "7:00"
# indicating when the alarm clock should ring. Weekdays, the alarm should be
# "7:00" and on the weekend it should be "10:00". Unless we are on vacation --
# then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
    pass


@pytest.mark.parametrize(
    "day,vacation,expected",
    [
        (1, False, "7:00"),
        (5, False, "7:00"),
        (0, False, "10:00"),
        (6, False, "10:00"),
        (0, True, "off"),
        (6, True, "off"),
        (1, True, "10:00"),
        (3, True, "10:00"),
        (5, True, "10:00"),
    ],
)
def test_alarm_clock(day, vacation, expected):
    assert alarm_clock(day, vacation) == expected
