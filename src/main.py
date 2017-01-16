
from Slice import Slice


def enum_slices_for_size(size):
    shapes = []
    for width in range(1, size + 1):
        if size % width == 0:
            hight = size / width
            shape = (width, hight)
            shapes.append(shape)
    return shapes


# return all possible shapes and sizes
def enum_slices(min_size, max_size):
    slices = []
    for size in range(min_size, max_size + 1):
        slices += enum_slices_for_size(size)
    return slices


def recurse(pizza):

    found_valid_slice = False

    for slice_type in SLICE_SIZES:

        for i in pizza.width:
            for j in pizza.height:

                # try put the slice here
                new_slice = Slice(i, j, *slice_type)

                if new_slice.is_valid():

                    found_valid_slice = True
                    return recurse(pizza.add_slice(new_slice))

    if not found_valid_slice:
        # No valid slice found for this pizza, this is the end

        return pizza.calculate_score()


SLICE_SIZES = []


def main():

    pizza = object()

    global SLICE_SIZES
    SLICE_SIZES = enum_slices(pizza.min_ingredients, pizza.max_cells_per_slice)
    recurse(pizza)


if __name__ == '__main__':
    main()
