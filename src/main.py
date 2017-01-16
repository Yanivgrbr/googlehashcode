from Slice import Slice
import Pizza


def print_output(out_file_path, pizza):
    with open(out_file_path, "wb") as out_file:
        num_of_slices = len(pizza.slices)
        out_file.write(num_of_slices + "\n")
        for p_slice in pizza.slices:
            out_file.write("%d %d %d %d\n" % (
                p_slice.top, p_slice.left, p_slice.bottom - 1, p_slice.right - 1))


def recurse(pizza):

    found_valid_slice = False

    for slice_width, slice_height in pizza.enum_slices():

        for i in xrange(pizza.num_of_rows):
            for j in xrange(pizza.num_of_cols):

                # try put the slice here
                new_slice = Slice(i, j, slice_width, slice_height)

                print "Trying slice at: (%d,%d) size: %d x %d" % (i, j, slice_width, slice_height)
                if pizza.is_valid(new_slice):
                    print "valid!"

                    found_valid_slice = True
                    return recurse(Pizza.add_slice(pizza, new_slice))

    if not found_valid_slice:
        # No valid slice found for this pizza, this is the end

        return pizza.get_num_of_taken_cells()


def main():

    pizza = Pizza.Pizza(3, 5, 1, 2, ["MMMMM", "MTTTM", "MMMMM"])
    print recurse(pizza)


if __name__ == '__main__':
    main()
