def custom_sort(lst, key_func):
    return sorted(lst, key=key_func)

example_list = ['apple', 'banana', 'cherry', 'date']
sorted_list = custom_sort(example_list, len)
print("Custom sorted list:", sorted_list)
