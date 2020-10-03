import pytest

# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of
# cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number
# of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
    pass


@pytest.mark.parametrize(
    "cigars,is_weekend,expected",
    [
        (30, False, False),
        (50, False, True),
        (70, True, True),
        (30, True, False),
        (50, True, True),
        (60, False, True),
        (61, False, False),
        (40, False, True),
        (39, False, False),
        (40, True, True),
        (39, True, False),
    ],
)
def test_cigar_party(cigars, is_weekend, expected):
    assert cigar_party(cigars, is_weekend) == expected
