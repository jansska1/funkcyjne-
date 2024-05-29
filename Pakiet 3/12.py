def rotate_list(lst, k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

example_list = [1, 2, 3, 4, 5]
rotated = rotate_list(example_list, 2)
print("Rotated list:", rotated)
