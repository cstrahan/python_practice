import pytest

# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.
def sum67(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2], 5),
        ([1, 2, 2, 6, 99, 99, 7], 5),
        ([1, 1, 6, 7, 2], 4),
        ([1, 6, 2, 2, 7, 1, 6, 99, 99, 7], 2),
        ([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7], 2),
        ([2, 7, 6, 2, 6, 7, 2, 7], 18),
        ([2, 7, 6, 2, 6, 2, 7], 9),
        ([1, 6, 7, 7], 8),
        ([6, 7, 1, 6, 7, 7], 8),
        ([6, 8, 1, 6, 7], 0),
        ([], 0),
        ([6, 7, 11], 11),
        ([11, 6, 7, 11], 22),
        ([2, 2, 6, 7, 7], 11),
    ],
)
def test_sum67(nums, expected):
    assert sum67(nums) == expected

