def countdown():
    """Write a generator that counts from 100 to 1"""
    number = 100
    while number >=\
            1:
        yield number
        number -= 1
