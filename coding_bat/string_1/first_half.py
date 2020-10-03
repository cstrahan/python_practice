import pytest

# Given a string of even length, return the first half.
# So the string "WooHoo" yields "Woo".
def first_half(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("WooHoo", "Woo"),
        ("HelloThere", "Hello"),
        ("abcdef", "abc"),
        ("ab", "a"),
        ("", ""),
        ("0123456789", "01234"),
        ("kitten", "kit"),
    ],
)
def test_first_half(str, expected):
    assert first_half(str) == expected
