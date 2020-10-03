import pytest

# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that
# come immediately after a 13 also do not count.
def sum13(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2, 1], 6),
        ([1, 1], 2),
        ([1, 2, 2, 1, 13], 6),
        ([1, 2, 13, 2, 1, 13], 4),
        ([13, 1, 2, 13, 2, 1, 13], 3),
        ([], 0),
        ([13], 0),
        ([13, 13], 0),
        ([13, 0, 13], 0),
        ([13, 1, 13], 0),
        ([5, 7, 2], 14),
        ([5, 13, 2], 5),
        ([0], 0),
        ([13, 0], 0),
    ],
)
def test_sum13(nums, expected):
    assert sum13(nums) == expected

