def multiply(x):
    return x * 5

def dividing(x):
    return x / 2

def compose(f, g):
    return lambda x: f(g(x))

r = compose(multiply, dividing)
print(r(5))
