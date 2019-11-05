from string import digits

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str: str) -> bool:
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    count = 0
    for w in input_str.lower():
        if w in VOWELS:
            count += 1
    if count == len(input_str):
        return True
    else:
        return False


def contains_any_py_chars(input_str: str) -> bool:
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for w in input_str.lower():
        if w in PYTHON:
            return True


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for n in input_str:
        if n in digits:
            return True
