import pathlib


def wc(file_):
    with open(file_) as file_handler:
        li = file_handler.read().splitlines(keepends=True)
        return f"{len(li)} {len([w for x in li for w in x.split()])} {len([element for char in li for element in char])} {file_.name}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys

    print(wc(sys.argv[1]))
