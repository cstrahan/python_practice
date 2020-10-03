import pytest

# Given a string and a non-negative int n, we'll say that the front of the
# string is the first 3 chars, or whatever is there if the string is less than
# length 3. Return n copies of the front;
def front_times(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("Chocolate", 2, "ChoCho"),
        ("Chocolate", 3, "ChoChoCho"),
        ("Abc", 3, "AbcAbcAbc"),
        ("Ab", 4, "AbAbAbAb"),
        ("A", 4, "AAAA"),
        ("", 4, ""),
        ("Abc", 0, ""),
    ],
)
def test_front_times(str, n, expected):
    assert front_times(str, n) == expected
