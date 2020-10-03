import pytest

# Given an array of ints, return True if 6 appears as either the first or last
# element in the array. The array will be length 1 or more.
def first_last6(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 6], True),
        ([6, 1, 2, 3], True),
        ([13, 6, 1, 2, 3], False),
        ([13, 6, 1, 2, 6], True),
        ([3, 2, 1], False),
        ([3, 6, 1], False),
        ([3, 6], True),
        ([6], True),
        ([3], False),
        ([5, 6], True),
        ([5, 5], False),
        ([1, 2, 3, 4, 6], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_first_last6(nums, expected):
    assert first_last6(nums) == expected
