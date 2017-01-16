import copy


class Tomato(object):
    pass


class Mushroom(object):
    pass


class Taken(object):
    pass


def add_slice(pizza, slice):
    new_pizza = copy.deepcopy(pizza)

    new_pizza.slices.append(slice)

    for x in range(slice.left, slice.right):
        for y in range(slice.bottom, slice.top):
            new_pizza.layout[x][y] = Taken()


class Pizza(object):
    def __init__(self, num_of_rows, num_of_cols, min_ingredients, max_cells_per_slice, layout):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.min_ingredients = min_ingredients
        self.max_cells_per_slice = max_cells_per_slice

        self.layout = []
        self.__build_pizza(layout)

        self.slices = []

    def __build_pizza(self, layout):
        for row in layout:
            next_row = []
            for col in row:
                if col == 'T':
                    next_row.append(Tomato())
                else:
                    next_row.append(Mushroom())
            self.layout.append(next_row)

    def get_ingredient(self, row, col):
        return self.layout[row][col]

    def get_num_of_taken_cells(self):
        taken_counter = 0

        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if isinstance(self.layout[row][col], Taken):
                    taken_counter += 1

        return taken_counter