import pytest

# Given an array of ints length 3, figure out which is larger, the first or last
# element in the array, and set all the other elements to be that value. Return
# the changed array.
def max_end3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [3, 3, 3]),
        ([11, 5, 9], [11, 11, 11]),
        ([2, 11, 3], [3, 3, 3]),
        ([11, 3, 3], [11, 11, 11]),
        ([3, 11, 11], [11, 11, 11]),
        ([2, 2, 2], [2, 2, 2]),
        ([2, 11, 2], [2, 2, 2]),
        ([0, 0, 1], [1, 1, 1]),
    ],
)
def test_max_end3(nums, expected):
    assert max_end3(nums) == expected
