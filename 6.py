arr = [1,2,3,4,5,6,7,8]
def square(x):
    return x ** 2

squared_list = map(square, arr)
print(list(squared_list))

