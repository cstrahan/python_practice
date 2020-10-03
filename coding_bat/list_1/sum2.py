import pytest

# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just
# sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], 3),
        ([1, 1], 2),
        ([1, 1, 1, 1], 2),
        ([1, 2], 3),
        ([1], 1),
        ([], 0),
        ([4, 5, 6], 9),
        ([4], 4),
    ],
)
def test_sum2(nums, expected):
    assert sum2(nums) == expected
