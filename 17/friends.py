from itertools import combinations, permutations


def friends_teams(arg, team_size: int = 2, order_does_matter: bool = False):
    if order_does_matter:
        return permutations(arg, team_size)
    else:
        return combinations(arg, team_size)
