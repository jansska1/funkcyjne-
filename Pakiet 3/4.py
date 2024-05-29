numbers = [1,2,1,3,4,5,3,6,4]
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

print(remove_duplicates(numbers))