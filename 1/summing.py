def sum_numbers(numbers=None):
    if numbers is not None:
        return sum(numbers)
    else:
        return sum(range(1, 101))
