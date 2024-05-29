numbers = [1, 2, 3, 4, 5, 6]

def map_nested(numbers):
    return list(map(lambda number: number ** 2, numbers))

print(map_nested(numbers))