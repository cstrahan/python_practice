import pytest

# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
    pass


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Bob", "Hello Bob!"),
        ("Alice", "Hello Alice!"),
        ("X", "Hello X!"),
        ("Dolly", "Hello Dolly!"),
        ("Alpha", "Hello Alpha!"),
        ("Omega", "Hello Omega!"),
        ("Goodbye", "Hello Goodbye!"),
        ("ho ho ho", "Hello ho ho ho!"),
        ("xyz!", "Hello xyz!!"),
        ("Hello", "Hello Hello!"),
    ],
)
def test_hello_name(name, expected):
    assert hello_name(name) == expected
