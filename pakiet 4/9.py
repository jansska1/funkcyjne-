def apply_to_tuples(lst, func):
    return [func(*t) for t in lst]

example_tuples = [(1, 2), (3, 4), (5, 6)]
applied = apply_to_tuples(example_tuples, lambda x, y: x + y)
print("Applied to tuples:", applied)
