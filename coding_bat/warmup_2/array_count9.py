import pytest

# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 9], 1),
        ([1, 9, 9], 2),
        ([1, 9, 9, 3, 9], 3),
        ([1, 2, 3], 0),
        ([], 0),
        ([4, 2, 4, 3, 1], 0),
        ([9, 2, 4, 3, 1], 1),
    ],
)
def test_array_count9(nums, expected):
    assert array_count9(nums) == expected
