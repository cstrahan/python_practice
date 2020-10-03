import pytest

# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears
# in the array somewhere.
def array123(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 2, 3, 1], True),
        ([1, 1, 2, 4, 1], False),
        ([1, 1, 2, 1, 2, 3], True),
        ([1, 1, 2, 1, 2, 1], False),
        ([1, 2, 3, 1, 2, 3], True),
        ([1, 2, 3], True),
        ([1, 1, 1], False),
        ([1, 2], False),
        ([1], False),
        ([], False),
    ],
)
def test_array123(nums, expected):
    assert array123(nums) == expected
