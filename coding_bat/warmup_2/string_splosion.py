import pytest

# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Code", "CCoCodCode"),
        ("abc", "aababc"),
        ("ab", "aab"),
        ("x", "x"),
        ("fade", "ffafadfade"),
        ("There", "TThTheTherThere"),
        ("Kitten", "KKiKitKittKitteKitten"),
        ("Bye", "BByBye"),
        ("Good", "GGoGooGood"),
        ("Bad", "BBaBad"),
    ],
)
def test_string_splosion(str, expected):
    assert string_splosion(str) == expected
