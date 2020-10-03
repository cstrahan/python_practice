import pytest

# Given an array of ints length 3, return an array with the elements "rotated
# left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [2, 3, 1]),
        ([5, 11, 9], [11, 9, 5]),
        ([7, 0, 0], [0, 0, 7]),
        ([1, 2, 1], [2, 1, 1]),
        ([0, 0, 1], [0, 1, 0]),
    ],
)
def test_rotate_left3(nums, expected):
    assert rotate_left3(nums) == expected
