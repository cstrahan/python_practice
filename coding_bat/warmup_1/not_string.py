import pytest

# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("candy", "not candy"),
        ("x", "not x"),
        ("not bad", "not bad"),
        ("bad", "not bad"),
        ("not", "not"),
        ("is not", "not is not"),
        ("no", "not no"),
    ],
)
def test_not_string(str, expected):
    assert not_string(str) == expected
