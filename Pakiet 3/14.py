def count_unique_elements(lst):
    return len(set(lst))

example_list = [1, 2, 2, 3, 4, 4, 5]
unique_count = count_unique_elements(example_list)
print("Unique elements count:", unique_count)