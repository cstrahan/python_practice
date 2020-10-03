import pytest

# Given an array length 1 or more of ints, return the difference between the
# largest and smallest values in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 3, 5, 6], 7),
        ([7, 2, 10, 9], 8),
        ([2, 10, 7, 2], 8),
        ([2, 10], 8),
        ([10, 2], 8),
        ([10, 0], 10),
        ([2, 3], 1),
        ([2, 2], 0),
        ([2], 0),
        ([5, 1, 6, 1, 9, 9], 8),
        ([7, 6, 8, 5], 3),
        ([7, 7, 6, 8, 5, 5, 6], 3),
    ],
)
def test_big_diff(nums, expected):
    assert big_diff(nums) == expected
