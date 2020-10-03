import pytest

# Return True if the string "cat" and "dog" appear the same number of times in
# the given string.
def cat_dog(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("catdog", True),
        ("catcat", False),
        ("1cat1cadodog", True),
        ("catxxdogxxxdog", False),
        ("catxdogxdogxcat", True),
        ("catxdogxdogxca", False),
        ("dogdogcat", False),
        ("dogogcat", True),
        ("dog", False),
        ("cat", False),
        ("ca", True),
        ("c", True),
        ("", True),
    ],
)
def test_cat_dog(str, expected):
    assert cat_dog(str) == expected
