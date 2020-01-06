from itertools import combinations


def find_number_pairs(numbers: list, N: int = 10) -> list:
    return [pair for pair in combinations(numbers, 2) if sum(pair) == N]
