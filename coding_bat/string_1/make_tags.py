import pytest

# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic
# text. In this example, the "i" tag makes <i> and </i> which surround the word
# "Yay". Given tag and word strings, create the HTML string with tags around the
# word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
    pass


@pytest.mark.parametrize(
    "tag,word,expected",
    [
        ("i", "Yay", "<i>Yay</i>"),
        ("i", "Hello", "<i>Hello</i>"),
        ("cite", "Yay", "<cite>Yay</cite>"),
        ("address", "here", "<address>here</address>"),
        ("body", "Heart", "<body>Heart</body>"),
        ("i", "i", "<i>i</i>"),
        ("i", "", "<i></i>"),
    ],
)
def test_make_tags(tag, word, expected):
    assert make_tags(tag, word) == expected
