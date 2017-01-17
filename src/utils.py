shapes = []


# return all possible shapes and sizes
def enum_shapes(pizza):
    global shapes
    # TODO: make more efficient
    for w in range(pizza.min_ingredients, pizza.max_cells_per_slice + 1):
        for h in range(pizza.min_ingredients, pizza.max_cells_per_slice + 1):
            if w * h >= pizza.min_ingredients * 2 and w * h <= pizza.max_cells_per_slice:
                shapes.append((w, h))

        # Drop all duplicates
        shapes = list(set(shapes))
