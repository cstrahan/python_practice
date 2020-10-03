import pytest

# Given a string, return a "rotated left 2" version where the first 2 chars are
# moved to the end. The string length will be at least 2.
def left2(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "lloHe"),
        ("java", "vaja"),
        ("Hi", "Hi"),
        ("code", "deco"),
        ("cat", "tca"),
        ("12345", "34512"),
        ("Chocolate", "ocolateCh"),
        ("bricks", "icksbr"),
    ],
)
def test_left2(str, expected):
    assert left2(str) == expected
