import pytest

# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], 6),
        ([5, 11, 2], 18),
        ([7, 0, 0], 7),
        ([1, 2, 1], 4),
        ([1, 1, 1], 3),
        ([2, 7, 2], 11),
    ],
)
def test_sum3(nums, expected):
    assert sum3(nums) == expected
