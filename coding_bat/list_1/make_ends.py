import pytest

# Given an array of ints, return a new array length 2 containing the first and
# last elements from the original array. The original array will be length 1 or
# more.
def make_ends(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4], [1, 4]),
        ([7, 4, 6, 2], [7, 2]),
        ([1, 2, 2, 2, 2, 2, 2, 3], [1, 3]),
        ([7, 4], [7, 4]),
        ([7], [7, 7]),
        ([5, 2, 9], [5, 9]),
        ([2, 3, 4, 1], [2, 1]),
    ],
)
def test_make_ends(nums, expected):
    assert make_ends(nums) == expected
