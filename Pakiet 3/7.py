def flatten_list(nested_list):
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

nested_list = [1, [2, [3, 4], 5], [6, 7], 8]
flattened = flatten_list(nested_list)
print(flattened)