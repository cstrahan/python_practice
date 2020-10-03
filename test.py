import pytest

# The parameter weekday is True if it is a weekday, and the parameter vacation
# is True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True


def sleep_in(weekday, vacation):
    pass


@pytest.mark.parametrize(
    "weekday,vacation,expected",
    [
        (False, False, True),
        (True, False, False),
        (False, True, True),
        (True, True, True),
    ],
)
def test_sleep_in(weekday, vacation, expected):
    assert sleep_in(weekday, vacation) == expected


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
# if each is smiling. We are in trouble if they are both smiling or if neither
# of them is smiling. Return True if we are in trouble.

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False


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


# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8


def sum_double(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (3, 2, 5),
        (2, 2, 8),
        (-1, 0, -1),
        (3, 3, 12),
        (0, 0, 0),
        (0, 1, 1),
        (3, 4, 7),
    ],
)
def test_sum_double(a, b, expected):
    assert sum_double(a, b) == expected


# Given an int n, return the absolute difference between n and 21, except return
# double the absolute difference if n is over 21.


def diff21(n):
    pass


@pytest.mark.parametrize(
    "n,expected",
    [
        (19, 2),
        (10, 11),
        (21, 0),
        (22, 2),
        (25, 8),
        (30, 18),
        (0, 21),
        (1, 20),
        (2, 19),
        (-1, 22),
        (-2, 23),
        (50, 58),
    ],
)
def test_diff21(n, expected):
    assert diff21(n) == expected


# We have a loud talking parrot. The "hour" parameter is the current hour time
# in the range 0..23. We are in trouble if the parrot is talking and the hour is
# before 7 or after 20. Return True if we are in trouble.


def parrot_trouble(talking, hour):
    pass


@pytest.mark.parametrize(
    "talking,hour,expected",
    [
        (True, 6, True),
        (True, 7, False),
        (False, 6, False),
        (True, 21, True),
        (False, 21, False),
        (False, 20, False),
        (True, 23, True),
        (False, 23, False),
        (True, 20, False),
        (False, 12, False),
    ],
)
def test_parrot_trouble(talking, hour, expected):
    assert parrot_trouble(talking, hour) == expected


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


def makes10(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (9, 10, True),
        (9, 9, False),
        (1, 9, True),
        (10, 1, True),
        (10, 10, True),
        (8, 2, True),
        (8, 3, False),
        (10, 42, True),
        (12, -2, True),
    ],
)
def test_makes10(a, b, expected):
    assert makes10(a, b) == expected


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num)
# computes the absolute value of a number.


def near_hundred(n):
    pass


@pytest.mark.parametrize(
    "n,expected",
    [
        (93, True),
        (90, True),
        (89, False),
        (110, True),
        (111, False),
        (121, False),
        (-101, False),
        (-209, False),
        (190, True),
        (209, True),
        (0, False),
        (5, False),
        (-50, False),
        (191, True),
        (189, False),
        (200, True),
        (210, True),
        (211, False),
        (290, False),
    ],
)
def test_near_hundred(n, expected):
    assert near_hundred(n) == expected


# Given 2 int values, return True if one is negative and one is positive. Except
# if the parameter "negative" is True, then return True only if both are
# negative.


def pos_neg(a, b, negative):
    pass


@pytest.mark.parametrize(
    "a,b,negative,expected",
    [
        (1, -1, False, True),
        (-1, 1, False, True),
        (-4, -5, True, True),
        (-4, -5, False, False),
        (-4, 5, False, True),
        (-4, 5, True, False),
        (1, 1, False, False),
        (-1, -1, False, False),
        (1, -1, True, False),
        (-1, 1, True, False),
        (1, 1, True, False),
        (-1, -1, True, True),
        (5, -5, False, True),
        (-6, 6, False, True),
        (-5, -6, False, False),
        (-2, -1, False, False),
        (1, 2, False, False),
        (-5, 6, True, False),
        (-5, -5, True, True),
    ],
)
def test_pos_neg(a, b, negative, expected):
    assert pos_neg(a, b, negative) == expected


# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.


def not_string(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("candy", "not candy"),
        ("x", "not x"),
        ("not bad", "not bad"),
        ("bad", "not bad"),
        ("not", "not"),
        ("is not", "not is not"),
        ("no", "not no"),
    ],
)
def test_not_string(str, expected):
    assert not_string(str) == expected


# Given a non-empty string and an int n, return a new string where the char at
# index n has been removed. The value of n will be a valid index of a char in
# the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


def missing_char(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("kitten", 1, "ktten"),
        ("kitten", 0, "itten"),
        ("kitten", 4, "kittn"),
        ("Hi", 0, "i"),
        ("Hi", 1, "H"),
        ("code", 0, "ode"),
        ("code", 1, "cde"),
        ("code", 2, "coe"),
        ("code", 3, "cod"),
        ("chocolate", 8, "chocolat"),
    ],
)
def test_missing_char(str, n, expected):
    assert missing_char(str, n) == expected


# Given a string, return a new string where the first and last chars have been exchanged.


def front_back(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("code", "eodc"),
        ("a", "a"),
        ("ab", "ba"),
        ("abc", "cba"),
        ("", ""),
        ("Chocolate", "ehocolatC"),
        ("aavJ", "Java"),
        ("hello", "oellh"),
    ],
)
def test_front_back(str, expected):
    assert front_back(str) == expected


# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there. Return a
# new string which is 3 copies of the front.


def front3(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Java", "JavJavJav"),
        ("Chocolate", "ChoChoCho"),
        ("abc", "abcabcabc"),
        ("abcXYZ", "abcabcabc"),
        ("ab", "ababab"),
        ("a", "aaa"),
        ("", ""),
    ],
)
def test_front3(str, expected):
    assert front3(str) == expected


# END OF WARMUP 1

# WARMUP 2

# Given a string and a non-negative int n, return a larger string that is n
# copies of the original string.


def string_times(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("Hi", 2, "HiHi"),
        ("Hi", 3, "HiHiHi"),
        ("Hi", 1, "Hi"),
        ("Hi", 0, ""),
        ("Hi", 5, "HiHiHiHiHi"),
        ("Oh Boy!", 2, "Oh Boy!Oh Boy!"),
        ("x", 4, "xxxx"),
        ("", 4, ""),
        ("code", 2, "codecode"),
        ("code", 3, "codecodecode"),
    ],
)
def test_string_times(str, n, expected):
    assert string_times(str, n) == expected


# Given a string and a non-negative int n, we'll say that the front of the
# string is the first 3 chars, or whatever is there if the string is less than
# length 3. Return n copies of the front;


def front_times(str, n):
    pass


@pytest.mark.parametrize(
    "str,n,expected",
    [
        ("Chocolate", 2, "ChoCho"),
        ("Chocolate", 3, "ChoChoCho"),
        ("Abc", 3, "AbcAbcAbc"),
        ("Ab", 4, "AbAbAbAb"),
        ("A", 4, "AAAA"),
        ("", 4, ""),
        ("Abc", 0, ""),
    ],
)
def test_front_times(str, n, expected):
    assert front_times(str, n) == expected


# Given a string, return a new string made of every other char starting with the
# first, so "Hello" yields "Hlo".


def string_bits(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "Hlo"),
        ("Hi", "H"),
        ("Heeololeo", "Hello"),
        ("HiHiHi", "HHH"),
        ("", ""),
        ("Greetings", "Getns"),
        ("Chocoate", "Coot"),
        ("pi", "p"),
        ("Hello Kitten", "HloKte"),
        ("hxaxpxpxy", "happy"),
    ],
)
def test_string_bits(str, expected):
    assert string_bits(str) == expected


# Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Code", "CCoCodCode"),
        ("abc", "aababc"),
        ("ab", "aab"),
        ("x", "x"),
        ("fade", "ffafadfade"),
        ("There", "TThTheTherThere"),
        ("Kitten", "KKiKitKittKitteKitten"),
        ("Bye", "BByBye"),
        ("Good", "GGoGooGood"),
        ("Bad", "BBaBad"),
    ],
)
def test_string_splosion(str, expected):
    assert string_splosion(str) == expected


# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string, so
# "hixxxhi" yields 1 (we won't count the end substring).


def last2(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("hixxhi", 1),
        ("xaxxaxaxx", 1),
        ("axxxaaxx", 2),
        ("xxaxxaxxaxx", 3),
        ("xaxaxaxx", 0),
        ("xxxx", 2),
        ("13121312", 1),
        ("11212", 1),
        ("13121311", 0),
        ("1717171", 2),
        ("hi", 0),
        ("h", 0),
        ("", 0),
    ],
)
def test_last2(str, expected):
    assert last2(str) == expected


# Given an array of ints, return the number of 9's in the array.


def array_count9(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 9], 1),
        ([1, 9, 9], 2),
        ([1, 9, 9, 3, 9], 3),
        ([1, 2, 3], 0),
        ([], 0),
        ([4, 2, 4, 3, 1], 0),
        ([9, 2, 4, 3, 1], 1),
    ],
)
def test_array_count9(nums, expected):
    assert array_count9(nums) == expected


# Given an array of ints, return True if one of the first 4 elements in the
# array is a 9. The array length may be less than 4.


def array_front9(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 9, 3, 4], True),
        ([1, 2, 3, 4, 9], False),
        ([1, 2, 3, 4, 5], False),
        ([9, 2, 3], True),
        ([1, 9, 9], True),
        ([1, 2, 3], False),
        ([1, 9], True),
        ([5, 5], False),
        ([2], False),
        ([9], True),
        ([], False),
        ([3, 9, 2, 3, 3], True),
    ],
)
def test_array_front9(nums, expected):
    assert array_front9(nums) == expected


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


# Given 2 strings, a and b, return the number of the positions where they
# contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since
# the "xx", "aa", and "az" substrings appear in the same place in both strings.


def string_match(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("xxcaazz", "xxbaaz", 3),
        ("abc", "abc", 2),
        ("abc", "axc", 0),
        ("hello", "he", 1),
        ("he", "hello", 1),
        ("h", "hello", 0),
        ("", "hello", 0),
        ("aabbccdd", "abbbxxd", 1),
        ("aaxxaaxx", "iaxxai", 3),
        ("iaxxai", "aaxxaaxx", 3),
    ],
)
def test_string_match(a, b, expected):
    assert string_match(a, b) == expected


# END, NOW STRING-1

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


# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns
# "HiByeByeHi".
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


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag
# makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around
# the word, e.g. "<i>Yay</i>".


def make_tags(tag, word):
    pass


@pytest.mark.parametrize(
    "tag,word,expected",
    [
        ("i", "Yay", "<i>Yay</i>"),
        ("i", "Hello", "<i>Hello</i>"),
        ("cite", "Yay", "<cite>Yay</cite>"),
        ("address", "here", "<address>here</address>"),
        ("body", "Heart", "<body>Heart</body>"),
        ("i", "i", "<i>i</i>"),
        ("i", "", "<i></i>"),
    ],
)
def test_make_tags(tag, word, expected):
    assert make_tags(tag, word) == expected


# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the
# out string, e.g. "<<word>>".
def make_out_word(out, word):
    pass


@pytest.mark.parametrize(
    "out,word,expected",
    [
        ("<<>>", "Yay", "<<Yay>>"),
        ("<<>>", "WooHoo", "<<WooHoo>>"),
        ("[[]]", "word", "[[word]]"),
        ("HHoo", "Hello", "HHHellooo"),
        ("abyz", "YAY", "abYAYyz"),
    ],
)
def test_make_out_word(out, word, expected):
    assert make_out_word(out, word) == expected


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length
# will be at least 2.
def extra_end(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "lololo"),
        ("ab", "ababab"),
        ("Hi", "HiHiHi"),
        ("Candy", "dydydy"),
        ("Code", "dedede"),
    ],
)
def test_extra_end(str, expected):
    assert extra_end(str) == expected


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is
# shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string
# "".
def first_two(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "He"),
        ("abcdefg", "ab"),
        ("ab", "ab"),
        ("a", "a"),
        ("", ""),
        ("Kitten", "Ki"),
        ("hi", "hi"),
        ("hiya", "hi"),
    ],
)
def test_first_two(str, expected):
    assert first_two(str) == expected


# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("WooHoo", "Woo"),
        ("HelloThere", "Hello"),
        ("abcdef", "abc"),
        ("ab", "a"),
        ("", ""),
        ("0123456789", "01234"),
        ("kitten", "kit"),
    ],
)
def test_first_half(str, expected):
    assert first_half(str) == expected


# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be
# at least 2.
def without_end(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "ell"),
        ("java", "av"),
        ("coding", "odin"),
        ("code", "od"),
        ("ab", ""),
        ("Chocolate!", "hocolate"),
        ("kitten", "itte"),
        ("woohoo", "ooho"),
    ],
)
def test_without_end(str, expected):
    assert without_end(str) == expected


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the
# longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hello", "hi", "hiHellohi"),
        ("hi", "Hello", "hiHellohi"),
        ("aaa", "b", "baaab"),
        ("b", "aaa", "baaab"),
        ("aaa", "", "aaa"),
        ("", "bb", "bb"),
        ("aaa", "1234", "aaa1234aaa"),
        ("aaa", "bb", "bbaaabb"),
        ("a", "bb", "abba"),
        ("bb", "a", "abba"),
        ("xyz", "ab", "abxyzab"),
    ],
)
def test_combo_string(a, b, expected):
    assert combo_string(a, b) == expected


# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length
# 1.
def non_start(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hello", "There", "ellohere"),
        ("java", "code", "avaode"),
        ("shotl", "java", "hotlava"),
        ("ab", "xy", "by"),
        ("ab", "x", "b"),
        ("x", "ac", "c"),
        ("a", "x", ""),
        ("kit", "kat", "itat"),
        ("mart", "dart", "artart"),
    ],
)
def test_non_start(a, b, expected):
    assert non_start(a, b) == expected


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will
# be at least 2.
def left2(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("Hello", "lloHe"),
        ("java", "vaja"),
        ("Hi", "Hi"),
        ("code", "deco"),
        ("cat", "tca"),
        ("12345", "34512"),
        ("Chocolate", "ocolateCh"),
        ("bricks", "icksbr"),
    ],
)
def test_left2(str, expected):
    assert left2(str) == expected


# LIST-1

# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be
# length 1 or more.
def first_last6(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 6], True),
        ([6, 1, 2, 3], True),
        ([13, 6, 1, 2, 3], False),
        ([13, 6, 1, 2, 6], True),
        ([3, 2, 1], False),
        ([3, 6, 1], False),
        ([3, 6], True),
        ([6], True),
        ([3], False),
        ([5, 6], True),
        ([5, 5], False),
        ([1, 2, 3, 4, 6], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_first_last6(nums, expected):
    assert first_last6(nums) == expected


# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are
# equal.
def same_first_last(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], False),
        ([1, 2, 3, 1], True),
        ([1, 2, 1], True),
        ([7], True),
        ([], False),
        ([1, 2, 3, 4, 5, 1], True),
        ([1, 2, 3, 4, 5, 13], False),
        ([13, 2, 3, 4, 5, 13], True),
        ([7, 7], True),
    ],
)
def test_same_first_last(nums, expected):
    assert same_first_last(nums) == expected


# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
    pass


def test_make_pi(expected):
    assert make_pi() == [3, 1, 4]


# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element.
# Both arrays will be length 1 or more.
def common_end(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1, 2, 3], [7, 3], True),
        ([1, 2, 3], [7, 3, 2], False),
        ([1, 2, 3], [1, 3], True),
        ([1, 2, 3], [1], True),
        ([1, 2, 3], [2], False),
    ],
)
def test_common_end(a, b, expected):
    assert common_end(a, b) == expected


# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], 6),
        ([5, 11, 2], 18),
        ([7, 0, 0], 7),
        ([1, 2, 1], 4),
        ([1, 1, 1], 3),
        ([2, 7, 2], 11),
    ],
)
def test_sum3(nums, expected):
    assert sum3(nums) == expected


# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [2, 3, 1]),
        ([5, 11, 9], [11, 9, 5]),
        ([7, 0, 0], [0, 0, 7]),
        ([1, 2, 1], [2, 1, 1]),
        ([0, 0, 1], [0, 1, 0]),
    ],
)
def test_rotate_left3(nums, expected):
    assert rotate_left3(nums) == expected


# Given an array of ints length 3, return a new array with the elements in reverse order,
# so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [3, 2, 1]),
        ([5, 11, 9], [9, 11, 5]),
        ([7, 0, 0], [0, 0, 7]),
        ([2, 1, 2], [2, 1, 2]),
        ([1, 2, 1], [1, 2, 1]),
        ([2, 11, 3], [3, 11, 2]),
        ([0, 6, 5], [5, 6, 0]),
        ([7, 2, 3], [3, 2, 7]),
    ],
)
def test_reverse3(nums, expected):
    assert reverse3(nums) == expected


# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the
# other elements to be that value. Return the changed array.
def max_end3(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [3, 3, 3]),
        ([11, 5, 9], [11, 11, 11]),
        ([2, 11, 3], [3, 3, 3]),
        ([11, 3, 3], [11, 11, 11]),
        ([3, 11, 11], [11, 11, 11]),
        ([2, 2, 2], [2, 2, 2]),
        ([2, 11, 2], [2, 2, 2]),
        ([0, 0, 1], [1, 1, 1]),
    ],
)
def test_max_end3(nums, expected):
    assert max_end3(nums) == expected


# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just
# sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], 3),
        ([1, 1], 2),
        ([1, 1, 1, 1], 2),
        ([1, 2], 3),
        ([1], 1),
        ([], 0),
        ([4, 5, 6], 9),
        ([4], 4),
    ],
)
def test_sum2(nums, expected):
    assert sum2(nums) == expected


# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([1, 2, 3], [4, 5, 6], [2, 5]),
        ([7, 7, 7], [3, 8, 0], [7, 8]),
        ([5, 2, 9], [1, 4, 5], [2, 4]),
        ([1, 9, 7], [4, 8, 8], [9, 8]),
        ([1, 2, 3], [3, 1, 4], [2, 1]),
        ([1, 2, 3], [4, 1, 1], [2, 1]),
    ],
)
def test_middle_way(a, b, expected):
    assert middle_way(a, b) == expected


# Given an array of ints, return a new array length 2 containing the first and last elements from the original array.
# The original array will be length 1 or more.
def make_ends(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3], [1, 3]),
        ([1, 2, 3, 4], [1, 4]),
        ([7, 4, 6, 2], [7, 2]),
        ([1, 2, 2, 2, 2, 2, 2, 3], [1, 3]),
        ([7, 4], [7, 4]),
        ([7], [7, 7]),
        ([5, 2, 9], [5, 9]),
        ([2, 3, 4, 1], [2, 1]),
    ],
)
def test_make_ends(nums, expected):
    assert make_ends(nums) == expected


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


# Logic-1

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


# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
# in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as
# an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With
# the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1
# (maybe).
def date_fashion(you, date):
    pass


@pytest.mark.parametrize(
    "you,date,expected",
    [
        (5, 10, 2),
        (5, 2, 0),
        (5, 5, 1),
        (3, 3, 1),
        (10, 2, 0),
        (2, 9, 0),
        (9, 9, 2),
        (10, 5, 2),
        (2, 2, 0),
        (3, 7, 1),
        (2, 7, 0),
        (6, 2, 0),
    ],
)
def test_date_fashion(you, date, expected):
    assert date_fashion(you, date) == expected


# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60
# and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a
# boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
    pass


@pytest.mark.parametrize(
    "temp,is_summer,expected",
    [
        (70, False, True),
        (95, False, False),
        (95, True, True),
        (90, False, True),
        (90, True, True),
        (50, False, False),
        (50, True, False),
        (100, False, False),
        (100, True, True),
        (105, True, False),
        (59, False, False),
        (59, True, False),
        (60, False, True),
    ],
)
def test_squirrel_play(temp, is_summer, expected):
    assert squirrel_play(temp, is_summer) == expected


# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int
# value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and
# 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day,
# your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    pass


@pytest.mark.parametrize(
    "speed,is_birthday,expected",
    [
        (60, False, 0),
        (65, False, 1),
        (65, True, 0),
        (80, False, 1),
        (85, False, 2),
        (85, True, 1),
        (70, False, 1),
        (75, False, 1),
        (75, True, 1),
        (40, False, 0),
        (40, True, 0),
        (90, False, 2),
    ],
)
def test_caught_speeding(speed, is_birthday, expected):
    assert caught_speeding(speed, is_birthday) == expected


# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case
# just return 20.
def sorta_sum(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 7),
        (9, 4, 20),
        (10, 11, 21),
        (12, -3, 9),
        (-3, 12, 9),
        (4, 5, 9),
        (4, 6, 20),
        (14, 7, 21),
        (14, 6, 20),
    ],
)
def test_sorta_sum(a, b, expected):
    assert sorta_sum(a, b) == expected


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation,
# return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and
# weekends it should be "off".
def alarm_clock(day, vacation):
    pass


@pytest.mark.parametrize(
    "day,vacation,expected",
    [
        (1, False, "7:00"),
        (5, False, "7:00"),
        (0, False, "10:00"),
        (6, False, "10:00"),
        (0, True, "off"),
        (6, True, "off"),
        (1, True, "10:00"),
        (3, True, "10:00"),
        (5, True, "10:00"),
    ],
)
def test_alarm_clock(day, vacation, expected):
    assert alarm_clock(day, vacation) == expected


# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum
# or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 4, True),
        (4, 5, False),
        (1, 5, True),
        (1, 6, True),
        (1, 8, False),
        (1, 7, True),
        (7, 5, False),
        (8, 2, True),
        (6, 6, True),
        (-6, 2, False),
        (-4, -10, True),
        (-7, 1, False),
        (7, -1, True),
        (-6, 12, True),
        (-2, -4, False),
        (7, 1, True),
        (0, 9, False),
        (8, 3, False),
        (3, 3, True),
        (3, 4, False),
    ],
)
def test_love6(a, b, expected):
    assert love6(a, b) == expected


# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return
# True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
    pass


@pytest.mark.parametrize(
    "n,outside_mode,expected",
    [
        (5, False, True),
        (11, False, False),
        (11, True, True),
        (10, False, True),
        (10, True, True),
        (9, False, True),
        (9, True, False),
        (1, False, True),
        (1, True, True),
        (0, False, False),
        (0, True, True),
        (-1, False, False),
        (-1, True, True),
        (99, False, False),
        (-99, True, True),
    ],
)
def test_in1to10(n, outside_mode, expected):
    assert in1to10(n, outside_mode) == expected


# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder
# of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
def near_ten(num):
    pass


@pytest.mark.parametrize(
    "num,expected",
    [
        (12, True),
        (17, False),
        (19, True),
        (31, True),
        (6, False),
        (10, True),
        (11, True),
        (21, True),
        (22, True),
        (23, False),
        (54, False),
        (155, False),
        (158, True),
        (3, False),
        (1, True),
    ],
)
def test_near_ten(num, expected):
    assert near_ten(num) == expected


# LOGIC-2

# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
# bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a
# little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks
def make_bricks(small, big, goal):
    pass


@pytest.mark.parametrize(
    "small,big,goal,expected",
    [
        (3, 1, 8, True),
        (3, 1, 9, False),
        (3, 2, 10, True),
        (3, 2, 8, True),
        (3, 2, 9, False),
        (6, 1, 11, True),
        (6, 0, 11, False),
        (1, 4, 11, True),
        (0, 3, 10, True),
        (1, 4, 12, False),
        (3, 1, 7, True),
        (1, 1, 7, False),
        (2, 1, 7, True),
        (7, 1, 11, True),
        (7, 1, 8, True),
        (7, 1, 13, False),
        (43, 1, 46, True),
        (40, 1, 46, False),
        (40, 2, 47, True),
        (40, 2, 50, True),
        (40, 2, 52, False),
        (22, 2, 33, False),
        (0, 2, 10, True),
        (1000000, 1000, 1000100, True),
        (2, 1000000, 100003, False),
        (20, 0, 19, True),
        (20, 0, 21, False),
        (20, 4, 51, False),
        (20, 4, 39, True),
    ],
)
def test_make_bricks(small, big, goal, expected):
    assert make_bricks(small, big, goal) == expected


# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it
# does not count towards the sum.
def lone_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (3, 2, 3, 2),
        (3, 3, 3, 0),
        (9, 2, 2, 9),
        (2, 2, 9, 9),
        (2, 9, 2, 9),
        (2, 9, 3, 14),
        (4, 2, 3, 9),
        (1, 3, 1, 3),
    ],
)
def test_lone_sum(a, b, c, expected):
    assert lone_sum(a, b, c) == expected


# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the
# sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (1, 2, 13, 3),
        (1, 13, 3, 1),
        (1, 13, 13, 1),
        (6, 5, 2, 13),
        (13, 2, 3, 0),
        (13, 2, 13, 0),
        (13, 13, 2, 0),
        (9, 4, 13, 13),
        (8, 13, 2, 8),
        (7, 2, 1, 10),
        (3, 3, 13, 6),
    ],
)
def test_lucky_sum(a, b, c, expected):
    assert lucky_sum(a, b, c) == expected


# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive
# -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def
# fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid
# repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the
# main no_teen_sum().
def no_teen_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 3, 6),
        (2, 13, 1, 3),
        (2, 1, 14, 3),
        (2, 1, 15, 18),
        (2, 1, 16, 19),
        (2, 1, 17, 3),
        (17, 1, 2, 3),
        (2, 15, 2, 19),
        (16, 17, 18, 16),
        (17, 18, 19, 0),
        (15, 16, 1, 32),
        (15, 15, 19, 30),
        (15, 19, 16, 31),
        (5, 17, 18, 5),
        (17, 18, 16, 16),
        (17, 19, 18, 0),
    ],
)
def test_no_teen_sum(a, b, c, expected):
    assert no_teen_sum(a, b, c) == expected


# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15
# rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12
# rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a
# separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level
# as round_sum().
def round_sum(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (16, 17, 18, 60),
        (12, 13, 14, 30),
        (6, 4, 4, 10),
        (4, 6, 5, 20),
        (4, 4, 6, 10),
        (9, 4, 4, 10),
        (0, 0, 1, 0),
        (0, 9, 0, 10),
        (10, 10, 19, 40),
        (20, 30, 40, 90),
        (45, 21, 30, 100),
        (23, 11, 26, 60),
        (23, 24, 25, 70),
        (25, 24, 25, 80),
        (23, 24, 29, 70),
        (11, 24, 36, 70),
        (24, 36, 32, 90),
        (14, 12, 26, 50),
        (12, 10, 24, 40),
    ],
)
def test_round_sum(a, b, c, expected):
    assert round_sum(a, b, c) == expected


# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is
# "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    pass


@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (1, 2, 10, True),
        (1, 2, 3, False),
        (4, 1, 3, True),
        (4, 5, 3, False),
        (4, 3, 5, False),
        (-1, 10, 0, True),
        (0, -1, 10, True),
        (10, 10, 8, True),
        (10, 8, 9, False),
        (8, 9, 10, False),
        (8, 9, 7, False),
        (8, 6, 9, True),
    ],
)
def test_close_far(a, b, c, expected):
    assert close_far(a, b, c) == expected


# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be
# done.
def make_chocolate(small, big, goal):
    pass


@pytest.mark.parametrize(
    "small,big,goal,expected",
    [
        (4, 1, 9, 4),
        (4, 1, 10, -1),
        (4, 1, 7, 2),
        (6, 2, 7, 2),
        (4, 1, 5, 0),
        (4, 1, 4, 4),
        (5, 4, 9, 4),
        (9, 3, 18, 3),
        (3, 1, 9, -1),
        (1, 2, 7, -1),
        (1, 2, 6, 1),
        (1, 2, 5, 0),
        (6, 1, 10, 5),
        (6, 1, 11, 6),
        (6, 1, 12, -1),
        (6, 1, 13, -1),
        (6, 2, 10, 0),
        (6, 2, 11, 1),
        (6, 2, 12, 2),
        (60, 100, 550, 50),
        (1000, 1000000, 5000006, 6),
        (7, 1, 12, 7),
        (7, 1, 13, -1),
        (7, 2, 13, 3),
    ],
)
def test_make_chocolate(small, big, goal, expected):
    assert make_chocolate(small, big, goal) == expected


# String-2

# Given a string, return a string where for every char in the original, there
# are two chars.
def double_char(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("The", "TThhee"),
        ("AAbb", "AAAAbbbb"),
        ("Hi-There", "HHii--TThheerree"),
        ("Word!", "WWoorrdd!!"),
        ("!!", "!!!!"),
        ("", ""),
        ("a", "aa"),
        (".", ".."),
        ("aa", "aaaa"),
    ],
)
def test_double_char(str, expected):
    assert double_char(str) == expected


# Return the number of times that the string "hi" appears anywhere in the given
# string.
def count_hi(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("abc hi ho", 1),
        ("ABChi hi", 2),
        ("hihi", 2),
        ("hiHIhi", 2),
        ("", 0),
        ("h", 0),
        ("hi", 1),
        ("Hi is no HI on ahI", 0),
        ("hiho not HOHIhi", 2),
    ],
)
def test_count_hi(str, expected):
    assert count_hi(str) == expected


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


# Return the number of times that the string "code" appears anywhere in the
# given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
# count.
def count_code(str):
    pass


@pytest.mark.parametrize(
    "str,expected",
    [
        ("aaacodebbb", 1),
        ("codexxcode", 2),
        ("cozexxcope", 2),
        ("cozfxxcope", 1),
        ("xxcozeyycop", 1),
        ("cozcop", 0),
        ("abcxyz", 0),
        ("code", 1),
        ("ode", 0),
        ("c", 0),
        ("", 0),
        ("AAcodeBBcoleCCccoreDD", 3),
        ("AAcodeBBcoleCCccorfDD", 2),
        ("coAcodeBcoleccoreDD", 3),
    ],
)
def test_count_code(str, expected):
    assert count_code(str) == expected


# Given two strings, return True if either of the strings appears at the very
# end of the other string, ignoring upper/lower case differences (in other
# words, the computation should not be "case sensitive"). Note: s.lower()
# returns the lowercase version of a string.
def end_other(a, b):
    pass


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("Hiabc", "abc", True),
        ("AbC", "HiaBc", True),
        ("abc", "abXabc", True),
        ("Hiabc", "abcd", False),
        ("Hiabc", "bc", True),
        ("Hiabcx", "bc", False),
        ("abc", "abc", True),
        ("xyz", "12xyz", True),
        ("yz", "12xz", False),
        ("Z", "12xz", True),
        ("12", "12", True),
        ("abcXYZ", "abcDEF", False),
        ("ab", "ab12", False),
        ("ab", "12ab", True),
    ],
)
def test_end_other(a, b, expected):
    assert end_other(a, b) == expected


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


# LIST-2

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


# Given an array length 1 or more of ints, return the difference between the
# largest and smallest values in the array. Note: the built-in min(v1, v2) and
# max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 3, 5, 6], 7),
        ([7, 2, 10, 9], 8),
        ([2, 10, 7, 2], 8),
        ([2, 10], 8),
        ([10, 2], 8),
        ([10, 0], 10),
        ([2, 3], 1),
        ([2, 2], 0),
        ([2], 0),
        ([5, 1, 6, 1, 9, 9], 8),
        ([7, 6, 8, 5], 3),
        ([7, 7, 6, 8, 5, 5, 6], 3),
    ],
)
def test_big_diff(nums, expected):
    assert big_diff(nums) == expected


# Return the "centered" average of an array of ints, which we'll say is the mean
# average of the values, except ignoring the largest and smallest values in the
# array. If there are multiple copies of the smallest value, ignore just one
# copy, and likewise for the largest value. Use int division to produce the
# final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4, 100], 3),
        ([1, 1, 5, 5, 10, 8, 7], 5),
        ([-10, -4, -2, -4, -2, 0], -3),
        ([5, 3, 4, 6, 2], 4),
        ([5, 3, 4, 0, 100], 4),
        ([100, 0, 5, 3, 4], 4),
        ([4, 0, 100], 4),
        ([0, 2, 3, 4, 100], 3),
        ([1, 1, 100], 1),
        ([7, 7, 7], 7),
        ([1, 7, 8], 7),
        ([1, 1, 99, 99], 50),
        ([1000, 0, 1, 99], 50),
        ([4, 4, 4, 4, 5], 4),
        ([4, 4, 4, 1, 5], 4),
        ([6, 4, 8, 12, 3], 6),
    ],
)
def test_centered_average(nums, expected):
    assert centered_average(nums) == expected


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


# Return the sum of the numbers in the array, except ignore sections of numbers
# starting with a 6 and extending to the next 7 (every 6 will be followed by at
# least one 7). Return 0 for no numbers.
def sum67(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2], 5),
        ([1, 2, 2, 6, 99, 99, 7], 5),
        ([1, 1, 6, 7, 2], 4),
        ([1, 6, 2, 2, 7, 1, 6, 99, 99, 7], 2),
        ([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7], 2),
        ([2, 7, 6, 2, 6, 7, 2, 7], 18),
        ([2, 7, 6, 2, 6, 2, 7], 9),
        ([1, 6, 7, 7], 8),
        ([6, 7, 1, 6, 7, 7], 8),
        ([6, 8, 1, 6, 7], 0),
        ([], 0),
        ([6, 7, 11], 11),
        ([11, 6, 7, 11], 22),
        ([2, 2, 6, 7, 7], 11),
    ],
)
def test_sum67(nums, expected):
    assert sum67(nums) == expected


# Given an array of ints, return True if the array contains a 2 next to a 2
# somewhere.
def has22(nums):
    pass


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 2], True),
        ([1, 2, 1, 2], False),
        ([2, 1, 2], False),
        ([2, 2, 1, 2], True),
        ([1, 3, 2], False),
        ([1, 3, 2, 2], True),
        ([2, 3, 2, 2], True),
        ([4, 2, 4, 2, 2, 5], True),
        ([1, 2], False),
        ([2, 2], True),
        ([2], False),
        ([], False),
        ([3, 3, 2, 2], True),
        ([5, 2, 5, 2], False),
    ],
)
def test_has22(nums, expected):
    assert has22(nums) == expected
