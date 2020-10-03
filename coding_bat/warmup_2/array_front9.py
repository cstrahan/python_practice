import pytest

# Given an array of ints, return True if one of the first 4 elements in the
# array is a 9. The array length may be less than 4.
def array_front9(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 9, 3, 4], True),
        ([1, 2, 3, 4, 9], False),
        ([1, 2, 3, 4, 5], False),
        ([9, 2, 3], True),
        ([1, 9, 9], True),
        ([1, 2, 3], False),
        ([1, 9], True),
        ([5, 5], False),
        ([2], False),
        ([9], True),
        ([], False),
        ([3, 9, 2, 3, 3], True),
    ],
)
def test_array_front9(nums, expected):
    assert array_front9(nums) == expected
