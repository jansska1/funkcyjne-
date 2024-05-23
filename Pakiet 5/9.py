from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

result = reduce(max, numbers)
print(result)

def avg(numb):
    return reduce(lambda x, y: x + y, numb) / len(numb)

print(avg(numbers))