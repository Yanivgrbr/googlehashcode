#!/usr/bin/python
import os
from Pizza import Pizza

# Current file path
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# Default file name
DEFAULT_INPUT_FILE_NAME = "..\input\small.in"


def read_input_file(file_name = DEFAULT_INPUT_FILE_NAME):
    '''
    Example:
        3 5 1 6
        TTTTT
        TMMMT
        TTTTT
    '''

    # Check if file exists
    if not os.path.isfile(file_name):
        file_name = DIR_PATH + "/" + file_name

    with open(file_name, "rb") as f:

        # Read configuration (row = 0)
        rows, columns, min_ingredients, max_cells_per_slice = f.readline().strip().split(" ")

        # List of rows
        list_rows = []

        # Read data (row = 1-n)
        while True:
            # Read next row
            next_row = f.readline().strip()

            # Check row is not empty (end of file)
            if not next_row:
                break

            # Populate arrays
            list_row = list(next_row)
            list_rows.append(list_row)

        # The pizza is in 'list_rows'
        pizza = Pizza(rows, columns, min_ingredients, max_cells_per_slice, list_rows)

        # Return pizza
        return pizza

def print_output(out_file_path, pizza):
    with open(out_file_path, "wb") as out_file:
        num_of_slices = len(pizza.slices)
        out_file.write(num_of_slices + "\n")
        for p_slice in pizza.slices:
            out_file.write("%d %d %d %d\n" % (
                p_slice.top, p_slice.left, p_slice.bottom, p_slice.right))