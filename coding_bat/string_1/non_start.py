import pytest

# Given 2 strings, return their concatenation, except omit the first char of
# each. The strings will be at least length 1.
def non_start(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hello", "There", "ellohere"),
        ("java", "code", "avaode"),
        ("shotl", "java", "hotlava"),
        ("ab", "xy", "by"),
        ("ab", "x", "b"),
        ("x", "ac", "c"),
        ("a", "x", ""),
        ("kit", "kat", "itat"),
        ("mart", "dart", "artart"),
    ],
)
def test_non_start(a, b, expected):
    assert non_start(a, b) == expected
