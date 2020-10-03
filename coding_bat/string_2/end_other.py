import pytest

# Given two strings, return True if either of the strings appears at the very
# end of the other string, ignoring upper/lower case differences (in other
# words, the computation should not be "case sensitive"). Note: s.lower()
# returns the lowercase version of a string.
def end_other(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hiabc", "abc", True),
        ("AbC", "HiaBc", True),
        ("abc", "abXabc", True),
        ("Hiabc", "abcd", False),
        ("Hiabc", "bc", True),
        ("Hiabcx", "bc", False),
        ("abc", "abc", True),
        ("xyz", "12xyz", True),
        ("yz", "12xz", False),
        ("Z", "12xz", True),
        ("12", "12", True),
        ("abcXYZ", "abcDEF", False),
        ("ab", "ab12", False),
        ("ab", "12ab", True),
    ],
)
def test_end_other(a, b, expected):
    assert end_other(a, b) == expected
