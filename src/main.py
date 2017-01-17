import time

import utils
from Pizza import Pizza, add_slice
from Slice import Slice
from parsing_utils import read_input_file
from utils import enum_shapes


DEBUG = False
list_pizzas = []

def print_output(out_file_path, pizza):
    with open(out_file_path, "wb") as out_file:
        num_of_slices = len(pizza.slices)
        out_file.write(num_of_slices + "\n")
        for p_slice in pizza.slices:
            out_file.write("%d %d %d %d\n" % (
                p_slice.top, p_slice.left, p_slice.bottom - 1, p_slice.right - 1))


def print_debug(data):
    if DEBUG:
        print data


def recurse(pizza, level=0):
    found_valid_slice = False


    # In every position
    for i in xrange(0, pizza.num_of_rows, 1):
        for j in xrange(0, pizza.num_of_cols, 1):

            # Skip this location if it's occupied
            # if pizza.is_taken(i, j):
            #     continue
            if pizza.get_ingredient(i, j) == 'X':
                continue

            # Try different sizes
            for slice_width, slice_height in utils.shapes:

                # Try new slice
                new_slice = Slice(i, j, slice_width, slice_height)

                # Debug print
                print_debug(
                    "%sTrying slice at: (%d,%d) size: %d x %d" % ("  " * level, i, j, slice_width, slice_height))

                # Check if slice is valid
                if pizza.is_valid(new_slice):
                    found_valid_slice = True
                    recurse(add_slice(pizza, new_slice), level + 1)

    # No valid slice found for this pizza, this is the end
    if not found_valid_slice:
        list_pizzas.append(pizza)


def get_best_pizza():
    max_slices = -1
    best_pizza = None

    for pizza in list_pizzas:
        # Get the best pizza slices arrangement
        if max_slices < pizza.get_num_of_taken_cells():
            best_pizza = pizza
            max_slices = pizza.get_num_of_taken_cells()

    return best_pizza


def get_demo_pizza():
    return Pizza(3, 5, 1, 6, [['T', 'T', 'T', 'T', 'T'],
                              ['T', 'M', 'M', 'M', 'T'],
                              ['T', 'T', 'T', 'T', 'T']])


def main():
    '''
    Coordinates
    ----------
    Because we are working with array of arrays,
        each inner array is a row in the 2D array.
        Therefore, first is the Y axis (row number), then comes the X axis (col number)

        (row,col) == (Y,X)
        (2,4) --> row number 2, column number 4

        Best practice would be to drop x,y terms and use only row,col terms
    '''

    # Timing
    time_start = time.time()

    # Allocate pizza
    pizza = get_demo_pizza()  # Demo
    # pizza = read_input_file("../input/small.in") #Small input
    # pizza = read_input_file("../input/medium.in")  # Medium input
    # pizza = read_input_file("../input/big.in")  # Big input

    # Create all shapes for pizza constraints
    enum_shapes(pizza)
    # Recursion
    recurse(pizza)

    # Timing
    time_end = time.time()

    # Get best result
    best_pizza = get_best_pizza()

    # Debug output
    print "-------------------"
    print "OUTPUT RESULTS (%s seconds)" % str(time_end - time_start)
    print "- There are %d different pizza possibilities." % len(list_pizzas)
    print "- The best pizza is:"
    print "     - Number of occupied cells: " + str(best_pizza.get_num_of_taken_cells())
    print "     - Slices: "
    for s in best_pizza.slices:
        print  "        " + str(s)

        # Output file
        # parser.print_output("output.txt", best_pizza)


if __name__ == '__main__':
    main()
    # import cProfile
    # cProfile.run("main()")
