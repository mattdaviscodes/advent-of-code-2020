ROWS = 128
COLS = 8

def binary_search(data_string, front_char, count):
    front = 0
    back = count -1

    for char in data_string[:7]:
        count //= 2
        if char == front_char:
            back -= count
        else:
            front += count

    return front

class Seat:
    def __init__(self, row=None, col=None):
        self.row = row
        self.col = col

    def __repr__(self):
        return repr('Seat(row={}, col={}, id={})'.format(self.row, self.col, self.id))

    @property
    def id(self):
        return self.row * 8 + self.col

    @classmethod
    def from_string(cls, data_string):
        row = binary_search(data_string[:7], 'F', ROWS)
        col = binary_search(data_string[-3:], 'L', COLS)

        return cls(row=row, col=col)