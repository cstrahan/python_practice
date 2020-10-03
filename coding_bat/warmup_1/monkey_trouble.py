import pytest

# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
# if each is smiling. We are in trouble if they are both smiling or if neither
# of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    pass


@pytest.mark.parametrize(
    "a_smile,b_smile,expected",
    [
        (True, True, True),
        (False, False, True),
        (True, False, False),
        (False, True, False),
    ],
)
def test_monkey_trouble(a_smile, b_smile, expected):
    assert monkey_trouble(a_smile, b_smile) == expected
