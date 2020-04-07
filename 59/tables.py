class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length
        self.first_row = [x for x in range(1, length + 1)]
        self.mult_table = []
        for i in range(1, length + 1):
            self.mult_table.append([str(i * x) for x in self.first_row])

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self.mult_table) * len(self.mult_table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        table_string = ""
        for i in range(self.length):
            table_string += " | ".join(self.mult_table[i]) + "\n"
        return table_string

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if x > len(self.mult_table) or y > len(self.mult_table[0]):
            raise IndexError
        return x * y
