def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    # new_list = my_cities + other_cities
    # new_list2 = set(my_cities + other_cities)
    # return len(new_list2) - (len(new_list) - len(new_list2))
    return len(set(my_cities) ^ set(other_cities))
