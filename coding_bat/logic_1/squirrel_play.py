import pytest

# The squirrels in Palo Alto spend most of the day playing. In particular, they
# play if the temperature is between 60 and 90 (inclusive). Unless it is summer,
# then the upper limit is 100 instead of 90. Given an int temperature and a
# boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
    pass


@pytest.mark.parametrize(
    "temp,is_summer,expected",
    [
        (70, False, True),
        (95, False, False),
        (95, True, True),
        (90, False, True),
        (90, True, True),
        (50, False, False),
        (50, True, False),
        (100, False, False),
        (100, True, True),
        (105, True, False),
        (59, False, False),
        (59, True, False),
        (60, False, True),
    ],
)
def test_squirrel_play(temp, is_summer, expected):
    assert squirrel_play(temp, is_summer) == expected
