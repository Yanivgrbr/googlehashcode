import copy


class Tomato(object):
    pass


class Mushroom(object):
    pass


class Taken(object):
    pass


def add_slice(pizza, pslice):
    #Todo: time consuming - must be more efficient

    # Memory copy
    new_pizza = copy.deepcopy(pizza)

    # Add new slice
    new_pizza.slices.append(pslice)

    # Update layout
    for row in range(pslice.top, pslice.bottom + 1):
        for col in range(pslice.left, pslice.right + 1):
            new_pizza.layout[row][col] = Taken()
    return new_pizza


class Pizza(object):
    def __init__(self, num_of_rows, num_of_cols, min_ingredients, max_cells_per_slice, layout):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.min_ingredients = min_ingredients
        self.max_cells_per_slice = max_cells_per_slice

        self.layout = []
        self.__build_pizza(layout)

        self.shapes = []
        self.slices = []

    def __build_pizza(self, layout):
        for row in layout:
            next_row = []
            for col in row:
                if col == 'T':
                    next_row.append(Tomato())
                elif col == 'M':
                    next_row.append(Mushroom())
                elif col == 'X':
                    next_row.append(Taken())
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

    # return all possible shapes and sizes
    def enum_shapes(self):
        # TODO: make more efficient

        if self.shapes == []:
            for w in range(self.min_ingredients, self.max_cells_per_slice + 1):
                for h in range(self.min_ingredients, self.max_cells_per_slice + 1):
                    if w*h >= self.min_ingredients * 2 and w*h <= self.max_cells_per_slice:
                        self.shapes.append((w,h))

            # Drop all duplicates
            self.shapes = set(self.shapes)

        return self.shapes

    def print_pizza(self):
        for i in self.layout:
            for j in i:
                if isinstance(j, Tomato):
                    print "T",
                else:
                    print "M",
            print ""

    def is_valid(self, pslice):
        '''
        - Doesn't exceed pizza's boundaries
        - Doesn't exceed maximum number of cells
        - Has minimum amount of tomatoes and mushrooms
        '''

        # Boundaries
        if pslice.left < 0 or pslice.top < 0:
            return False

        if pslice.right >= self.num_of_cols or pslice.bottom >= self.num_of_rows:
            return False

        # Maximum # of cells
        if pslice.width * pslice.height > self.max_cells_per_slice:
            return False

        # Enough mushrooms & tomatoes
        number_of_tomatoes = 0
        number_of_mushrooms = 0
        is_enough_ingredients = False

        for row in range(pslice.top, pslice.bottom + 1):
            for col in range(pslice.left, pslice.right + 1):

                ingredient = self.get_ingredient(row, col)

                if type(ingredient) == Taken:
                    return False

                elif type(ingredient) == Mushroom:
                    number_of_mushrooms += 1

                elif type(ingredient) == Tomato:
                    number_of_tomatoes += 1

            # Speed things up
            if number_of_tomatoes >= self.min_ingredients and number_of_mushrooms >= self.min_ingredients:
                is_enough_ingredients = True
                break

        if not is_enough_ingredients:
            return False

        # Nothing failed, all's good!
        return True
