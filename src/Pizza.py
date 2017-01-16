class Tomato(object):
    pass


class Mushroom(object):
    pass


class Pizza(object):
    def __init__(self, num_of_rows, num_of_cols, min_ingredients, max_cells_per_slice, pizza_layout):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.min_ingredients = min_ingredients
        self.max_cells_per_slice = max_cells_per_slice

        self.__pizza_layout = []
        self.__build_pizza(pizza_layout)

    def __build_pizza(self, pizza_layout):
        for row in pizza_layout:
            next_row = []
            for col in row:
                if col == 'T':
                    next_row.append(Tomato())
                else:
                    next_row.append(Mushroom())
            self.__pizza_layout.append(next_row)

    def get_ingredient(self, row, col):
        return self.__pizza_layout[row][col]