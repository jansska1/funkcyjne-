numbers = [[1,2,3],[2,3,4,5]]
def recursive_sum(numbers):
    return sum(sum(sublist) for sublist in numbers)

print(recursive_sum(numbers))