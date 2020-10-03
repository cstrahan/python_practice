import pytest

# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as
# an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With
# the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1
# (maybe).
def date_fashion(you, date):
    pass


@pytest.mark.parametrize(
    "you,date,expected",
    [
        (5, 10, 2),
        (5, 2, 0),
        (5, 5, 1),
        (3, 3, 1),
        (10, 2, 0),
        (2, 9, 0),
        (9, 9, 2),
        (10, 5, 2),
        (2, 2, 0),
        (3, 7, 1),
        (2, 7, 0),
        (6, 2, 0),
    ],
)
def test_date_fashion(you, date, expected):
    assert date_fashion(you, date) == expected
