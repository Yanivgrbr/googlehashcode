
from Slice import Slice
import Pizza


def recurse(pizza):

    found_valid_slice = False

    for slice_type in pizza.enum_slices():

        for i in xrange(pizza.num_of_rows):
            for j in xrange(pizza.num_of_cols):

                # try put the slice here
                new_slice = Slice(i, j, *slice_type)

                print "Trying slice at: (%d %d) %d by %d" % (i, j, *slice_type)
                if pizza.is_valid(new_slice):


                    found_valid_slice = True
                    return recurse(Pizza.add_slice(pizza, new_slice))

    if not found_valid_slice:
        # No valid slice found for this pizza, this is the end

        return pizza.get_num_of_taken_cells()


def main():

    import pdb; pdb.set_trace()
    pizza = Pizza.Pizza(3, 4, 1, 2, ["TTTM", "MMMT", "TTMM"])
    print recurse(pizza)


if __name__ == '__main__':
    main()
