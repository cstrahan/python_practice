import pytest

# Return True if the given string contains an appearance of "xyz" where the xyz
# is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does
# not.
def xyz_there(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("abcxyz", True),
        ("abc.xyz", False),
        ("xyz.abc", True),
        ("abcxy", False),
        ("xyz", True),
        ("xy", False),
        ("x", False),
        ("", False),
        ("abc.xyzxyz", True),
        ("abc.xxyz", True),
        (".xyz", False),
        ("12.xyz", False),
        ("12xyz", True),
        ("1.xyz.xyz2.xyz", False),
    ],
)
def test_xyz_there(str, expected):
    assert xyz_there(str) == expected
