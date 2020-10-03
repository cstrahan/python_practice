import pytest

# Given an "out" string length 4, such as "<<>>", and a word, return a new
# string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
    pass


@pytest.mark.parametrize(
    "out,word,expected",
    [
        ("<<>>", "Yay", "<<Yay>>"),
        ("<<>>", "WooHoo", "<<WooHoo>>"),
        ("[[]]", "word", "[[word]]"),
        ("HHoo", "Hello", "HHHellooo"),
        ("abyz", "YAY", "abYAYyz"),
    ],
)
def test_make_out_word(out, word, expected):
    assert make_out_word(out, word) == expected
