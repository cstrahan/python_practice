import pytest

# Return the "centered" average of an array of ints, which we'll say is the mean
# average of the values, except ignoring the largest and smallest values in the
# array. If there are multiple copies of the smallest value, ignore just one
# copy, and likewise for the largest value. Use int division to produce the
# final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4, 100], 3),
        ([1, 1, 5, 5, 10, 8, 7], 5),
        ([-10, -4, -2, -4, -2, 0], -3),
        ([5, 3, 4, 6, 2], 4),
        ([5, 3, 4, 0, 100], 4),
        ([100, 0, 5, 3, 4], 4),
        ([4, 0, 100], 4),
        ([0, 2, 3, 4, 100], 3),
        ([1, 1, 100], 1),
        ([7, 7, 7], 7),
        ([1, 7, 8], 7),
        ([1, 1, 99, 99], 50),
        ([1000, 0, 1, 99], 50),
        ([4, 4, 4, 4, 5], 4),
        ([4, 4, 4, 1, 5], 4),
        ([6, 4, 8, 12, 3], 6),
    ],
)
def test_centered_average(nums, expected):
    assert centered_average(nums) == expected
