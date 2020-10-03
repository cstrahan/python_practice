import pytest

# Given 2 strings, a and b, return a string of the form short+long+short, with
# the shorter string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hello", "hi", "hiHellohi"),
        ("hi", "Hello", "hiHellohi"),
        ("aaa", "b", "baaab"),
        ("b", "aaa", "baaab"),
        ("aaa", "", "aaa"),
        ("", "bb", "bb"),
        ("aaa", "1234", "aaa1234aaa"),
        ("aaa", "bb", "bbaaabb"),
        ("a", "bb", "abba"),
        ("bb", "a", "abba"),
        ("xyz", "ab", "abxyzab"),
    ],
)
def test_combo_string(a, b, expected):
    assert combo_string(a, b) == expected
