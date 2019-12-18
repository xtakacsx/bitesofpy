from typing import List

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names: List[str]):
    # test_list = []
    # for name in names:
    #     if name[0].lower() == QUIT_CHAR:
    #         break
    #     if name[0].lower() != IGNORE_CHAR and not any(char.isdigit() for char in name):
    #         test_list.append(name)
    #
    # return test_list[:MAX_NAMES]
    count = 0
    for name in names:
        if name.startswith(IGNORE_CHAR) or any(char.isdigit() for char in name):
            continue
        elif name.startswith(QUIT_CHAR) or count >= MAX_NAMES:
            break
        count += 1
        yield name
