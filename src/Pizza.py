def add_slice(pizza, pslice):
    #Todo: time consuming - must be more efficient

    # Memory copy
    layout = [row[:] for row in pizza.layout]
    new_pizza = Pizza(pizza.num_of_rows, pizza.num_of_cols, pizza.min_ingredients, pizza.max_cells_per_slice, layout)
    # new_pizza = copy.deepcopy(pizza)

    # Add slices from old pizza
    for old_slice in pizza.slices:
        new_pizza.slices.append(old_slice)
    # Add new slice
    new_pizza.slices.append(pslice)

    # Update layout
    for row in range(pslice.top, pslice.bottom + 1):
        for col in range(pslice.left, pslice.right + 1):
            new_pizza.layout[row][col] = 'X'
    return new_pizza


class Pizza(object):
    def __init__(self, num_of_rows, num_of_cols, min_ingredients, max_cells_per_slice, layout):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols
        self.min_ingredients = min_ingredients
        self.max_cells_per_slice = max_cells_per_slice

        self.layout = layout

        self.shapes = []
        self.slices = []

    def get_ingredient(self, row, col):
        return self.layout[row][col]

    def is_taken(self, x, y):
        # Search if point is in any of the slices
        for pslice in self.slices:
            if pslice.is_inside(x, y):
                return True
        return False

    def get_num_of_taken_cells(self):
        taken_counter = 0

        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.layout[row][col] == 'X':
                    taken_counter += 1

        return taken_counter

    def print_pizza(self):
        for i in self.layout:
            for j in i:
                print j
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

                # if self.is_taken(row, col):
                #     return False

                ingredient = self.get_ingredient(row, col)

                if ingredient == 'X':
                    return False

                if ingredient == 'M':
                    number_of_mushrooms += 1

                else:
                    number_of_tomatoes += 1

            # Speed things up
            if number_of_tomatoes >= self.min_ingredients and number_of_mushrooms >= self.min_ingredients:
                is_enough_ingredients = True
                break

        if not is_enough_ingredients:
            return False

        # Nothing failed, all's good!
        return True
