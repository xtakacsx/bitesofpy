import itertools


def find_number_pairs(numbers: list, N: int = 10) -> list:
    comb = itertools.combinations(numbers, 2)
    return [(n1, n2) for n1, n2 in comb if n1 + n2 == N]
