import pytest

# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string, so
# "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("hixxhi", 1),
        ("xaxxaxaxx", 1),
        ("axxxaaxx", 2),
        ("xxaxxaxxaxx", 3),
        ("xaxaxaxx", 0),
        ("xxxx", 2),
        ("13121312", 1),
        ("11212", 1),
        ("13121311", 0),
        ("1717171", 2),
        ("hi", 0),
        ("h", 0),
        ("", 0),
    ],
)
def test_last2(str, expected):
    assert last2(str) == expected
