import pytest

# Return the number of even ints in the given array. Note: the % "mod" operator
# computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 1, 2, 3, 4], 3),
        ([2, 2, 0], 3),
        ([1, 3, 5], 0),
        ([], 0),
        ([11, 9, 0, 1], 1),
        ([2, 11, 9, 0], 2),
        ([2], 1),
        ([2, 5, 12], 2),
    ],
)
def test_count_evens(nums, expected):
    assert count_evens(nums) == expected
