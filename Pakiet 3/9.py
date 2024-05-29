def zip_with_index(lst):
    return [(index, item) for index, item in enumerate(lst)]

example_list = ['a', 'b', 'c', 'd']
zipped = zip_with_index(example_list)
print(zipped)
