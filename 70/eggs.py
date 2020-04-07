from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.limit:
            raise StopIteration
        else:
            self.current += 1
            return choice(COLORS)


for egg in EggCreator(8):
    print(egg)
