from Slice import Slice
import Pizza

array_pizzas = []

def print_output(out_file_path, pizza):
    with open(out_file_path, "wb") as out_file:
        num_of_slices = len(pizza.slices)
        out_file.write(num_of_slices + "\n")
        for p_slice in pizza.slices:
            out_file.write("%d %d %d %d\n" % (
                p_slice.top, p_slice.left, p_slice.bottom - 1, p_slice.right - 1))


def recurse(pizza, level = 0):

    found_valid_slice = False

    for slice_width, slice_height in pizza.enum_slices():

        for i in xrange(pizza.num_of_rows):
            for j in xrange(pizza.num_of_cols):

                # try put the slice here
                new_slice = Slice(i, j, slice_width, slice_height)

                print "%sTrying slice at: (%d,%d) size: %d x %d" % ("  " * level, i ,j, slice_width, slice_height),
                if pizza.is_valid(new_slice):
                    print " - Valid!"

                    found_valid_slice = True
                    recurse(Pizza.add_slice(pizza, new_slice), level+1)
                else:
                    print ""

    if not found_valid_slice:
        # No valid slice found for this pizza, this is the end
        array_pizzas.append(pizza)

def get_best_pizza():
    max_slices = -1
    best_pizza = None

    for pizza in array_pizzas:
        # Get the best pizza slices arrangement
        if max_slices < pizza.get_num_of_taken_cells():
            best_pizza = pizza
            max_slices = pizza.get_num_of_taken_cells()

    return best_pizza


def main():

    # Allocate pizza
    pizza = Pizza.Pizza(3, 5, 1, 6, ["TTTTT", "TMMMT", "TTTTT"])

    # Recursion
    recurse(pizza)

    # Get best result
    best_pizza = get_best_pizza()

    # Debug output
    print "-------------------"
    print "The best pizza is:"
    print "     # of taken cells: " + str(best_pizza.get_num_of_taken_cells())
    print "     slices: "
    for s in best_pizza.slices:
        print  "        " + str(s)


if __name__ == '__main__':
    main()
