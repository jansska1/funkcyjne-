def add(a, b):
    return a + b

def sum(f, a, b):
    return f(a,b)

r = sum(add, 2, 5)
print(r)