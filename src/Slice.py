class Slice(object):
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    @property
    def left(self):
        return self.col

    @property
    def right(self):
        return self.col + self.width - 1

    @property
    def top(self):
        return self.row

    @property
    def bottom(self):
        return self.row + self.height - 1

    def grow_right(self):
        self.width += 1

    def grow_left(self):
        self.col -= 1

    def grow_up(self):
        self.yrow-= 1

    def grow_down(self):
        self.height += 1

    def __str__(self):
        return "[(%d,%d),(%d,%d)]" % (self.top, self.left, self.bottom, self.right)