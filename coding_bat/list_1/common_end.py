import pytest

# Given 2 arrays of ints, a and b, return True if they have the same first
# element or they have the same last element. Both arrays will be length 1 or
# more.
def common_end(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1, 2, 3], [7, 3], True),
        ([1, 2, 3], [7, 3, 2], False),
        ([1, 2, 3], [1, 3], True),
        ([1, 2, 3], [1], True),
        ([1, 2, 3], [2], False),
    ],
)
def test_common_end(a, b, expected):
    assert common_end(a, b) == expected
