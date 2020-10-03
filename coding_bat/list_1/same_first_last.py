import pytest

# Given an array of ints, return True if the array is length 1 or more, and the
# first element and the last element are equal.
def same_first_last(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], False),
        ([1, 2, 3, 1], True),
        ([1, 2, 1], True),
        ([7], True),
        ([], False),
        ([1, 2, 3, 4, 5, 1], True),
        ([1, 2, 3, 4, 5, 13], False),
        ([13, 2, 3, 4, 5, 13], True),
        ([7, 7], True),
    ],
)
def test_same_first_last(nums, expected):
    assert same_first_last(nums) == expected
