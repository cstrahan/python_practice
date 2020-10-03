import pytest

# Return the number of times that the string "hi" appears anywhere in the given
# string.
def count_hi(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("abc hi ho", 1),
        ("ABChi hi", 2),
        ("hihi", 2),
        ("hiHIhi", 2),
        ("", 0),
        ("h", 0),
        ("hi", 1),
        ("Hi is no HI on ahI", 0),
        ("hiho not HOHIhi", 2),
    ],
)
def test_count_hi(str, expected):
    assert count_hi(str) == expected
