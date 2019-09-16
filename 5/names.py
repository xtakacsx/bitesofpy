import operator

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names: list) -> list:
    """Should return a list of title cased names,
       each name appears only once"""

    # return_list = []
    # for name in names:
    #     x = ""
    #     for s in name.split(' '):
    #         x += f" {s.capitalize()}"
    #     return_list.append(x.strip())
    # return list(set(return_list))
    return list({name.title() for name in names})


def sort_by_surname_desc(names: list) -> list:
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    # return_dic = {}
    # for s in names:
    #     name, surname = s.split(" ")
    #     return_dic[name] = surname
    # return [f"{x} {v}" for x, v in sorted(return_dic.items(), key=operator.itemgetter(1), reverse=True)]
    return sorted(names, key=lambda x: x.split()[-1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    # return_list = []
    # for s in names:
    #     name, surname = s.split(" ")
    #     return_list.append(name)
    # return sorted(return_list, key=len)[0]
    return min([name.split()[0] for name in names], key=len)
