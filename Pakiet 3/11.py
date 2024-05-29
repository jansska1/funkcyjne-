def find_max_min_diff(lst):
    return max(lst) - min(lst)

example_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_min_diff = find_max_min_diff(example_list)
print("Max-Min difference:", max_min_diff)