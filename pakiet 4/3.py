def filter_even_values(d):
    return {k: v for k, v in d.items() if v % 2 == 0}

example_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_even_values(example_dict)
print("Filtered dictionary:", filtered_dict)