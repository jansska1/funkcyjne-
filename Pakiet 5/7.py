numbers = [1, 2, 3, 4, 5, 6, 7, 8]
def square(x):
    return x ** 2

def addingFive(x):
    return x + 5

def func_connected(numbers, *functions):
    results = []
    for num in numbers:
        result = num
        for func in functions:
            result = func(result)
        results.append(result)
    return results

result = func_connected(numbers, square, addingFive)
print(result)
