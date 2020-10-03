import pytest

# Given a string, return a new string made of every other char starting with the
# first, so "Hello" yields "Hlo".
def string_bits(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "Hlo"),
        ("Hi", "H"),
        ("Heeololeo", "Hello"),
        ("HiHiHi", "HHH"),
        ("", ""),
        ("Greetings", "Getns"),
        ("Chocoate", "Coot"),
        ("pi", "p"),
        ("Hello Kitten", "HloKte"),
        ("hxaxpxpxy", "happy"),
    ],
)
def test_string_bits(str, expected):
    assert string_bits(str) == expected
