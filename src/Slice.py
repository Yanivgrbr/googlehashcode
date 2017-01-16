class Slice(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x+self.width

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y+self.height

    def grow_right(self):
        self.width += 1

    def grow_left(self):
        self.x -= 1

    def grow_up(self):
        self.y -= 1

    def grow_down(self):
        self.height += 1
