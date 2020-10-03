import pytest

# Given 2 int arrays, a and b, each length 3, return a new array length 2
# containing their middle elements.
def middle_way(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1, 2, 3], [4, 5, 6], [2, 5]),
        ([7, 7, 7], [3, 8, 0], [7, 8]),
        ([5, 2, 9], [1, 4, 5], [2, 4]),
        ([1, 9, 7], [4, 8, 8], [9, 8]),
        ([1, 2, 3], [3, 1, 4], [2, 1]),
        ([1, 2, 3], [4, 1, 1], [2, 1]),
    ],
)
def test_middle_way(a, b, expected):
    assert middle_way(a, b) == expected
