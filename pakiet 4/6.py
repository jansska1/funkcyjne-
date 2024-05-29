def map_function(lst, func):
    return [func(x) for x in lst]

example_list = [1, 2, 3, 4, 5]
mapped = map_function(example_list, lambda x: x * x)
print("Mapped list:", mapped)