import pytest

# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 5], True),
        ([4, 3], True),
        ([4, 5], False),
        ([2, 2], True),
        ([3, 2], True),
        ([3, 3], True),
        ([7, 7], False),
        ([3, 9], True),
        ([9, 5], False),
    ],
)
def test_has23(nums, expected):
    assert has23(nums) == expected
