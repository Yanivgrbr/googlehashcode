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

    def is_valid(self, slice):
        '''
        - Doesn't exceed pizza's boundaries
        - Doesn't exceed maximum number of cells
        - Has minimum amount of tomatoes and mushrooms
        '''

        # Boundaries
        if slice.left < 0 or slice.top < 0:
            return False

        if slice.right >= self.num_of_rows or slice.bottom >= self.num_of_rows:
            return False

        # Maximum # of cells
        if slice.width * slice.height > self.max_cells_per_slice:
            return False

        # Enough mushrooms & tomatoes
        number_of_tomatoes = 0
        number_of_mushrooms = 0
        for col in xrange(slice.width + 1):
            for row in xrange(slice.height + 1):
                ingredient = self.get_ingredient(self.top + row, slice.left + col)

                if type(ingredient) == Mushroom:
                    number_of_mushrooms += 1

                if type(ingredient) == Tomato:
                    number_of_tomatoes += 1


        if number_of_tomatoes < self.min_ingredients or number_of_mushrooms < self.min_ingredients:
            return False


        # Nothing failed, all's good!
        return True