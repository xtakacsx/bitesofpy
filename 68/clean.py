import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    for element in input_string:
        if element in string.punctuation:
            input_string = input_string.replace(element, '')
    return input_string
