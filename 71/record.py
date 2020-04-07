class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.cache = []

    def __call__(self, n):
        if n not in self.cache:
            self.cache.append(n)
        return max(self.cache)
