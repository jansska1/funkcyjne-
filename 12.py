from functools import partial
def multiply(x, y):
    return x * y

pF = partial(multiply, 10)

print(pF(3))
