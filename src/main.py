
from Slice import Slice
from Pizza import Pizza


def recurse(pizza):

    found_valid_slice = False

    for slice_type in pizza.enum_slices():

        for i in xrange(pizza.num_of_rows):
            for j in xrange(pizza.num_of_cols):

                # try put the slice here
                new_slice = Slice(i, j, *slice_type)

                if new_slice.is_valid():

                    found_valid_slice = True
                    return recurse(pizza.add_slice(new_slice))

    if not found_valid_slice:
        # No valid slice found for this pizza, this is the end

        return pizza.calculate_score()


def main():

    pizza = Pizza(4, 4, 2, 3, ["TTTM", "MMMT", "TTMM"])
    recurse(pizza)


if __name__ == '__main__':
    main()
