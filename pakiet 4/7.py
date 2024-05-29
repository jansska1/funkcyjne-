def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_dict)