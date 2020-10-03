import pytest

# Given two strings, a and b, return the result of putting them together in the
# order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hi", "Bye", "HiByeByeHi"),
        ("Yo", "Alice", "YoAliceAliceYo"),
        ("What", "Up", "WhatUpUpWhat"),
        ("aaa", "bbb", "aaabbbbbbaaa"),
        ("x", "y", "xyyx"),
        ("x", "", "xx"),
        ("", "y", "yy"),
        ("Bo", "Ya", "BoYaYaBo"),
        ("Ya", "Ya", "YaYaYaYa"),
    ],
)
def test_make_abba(a, b, expected):
    assert make_abba(a, b) == expected
