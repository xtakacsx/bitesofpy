import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        self._numbers.insert(bisect.bisect(self._numbers, num), num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)
