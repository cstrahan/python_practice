import pytest

# Return the number of times that the string "code" appears anywhere in the
# given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
# count.
def count_code(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("aaacodebbb", 1),
        ("codexxcode", 2),
        ("cozexxcope", 2),
        ("cozfxxcope", 1),
        ("xxcozeyycop", 1),
        ("cozcop", 0),
        ("abcxyz", 0),
        ("code", 1),
        ("ode", 0),
        ("c", 0),
        ("", 0),
        ("AAcodeBBcoleCCccoreDD", 3),
        ("AAcodeBBcoleCCccorfDD", 2),
        ("coAcodeBcoleccoreDD", 3),
    ],
)
def test_count_code(str, expected):
    assert count_code(str) == expected
