from itertools import product

listItem = [1,2,3]
def connect(listItem):
    return list(product(listItem, repeat = 2,))

print(connect(listItem))