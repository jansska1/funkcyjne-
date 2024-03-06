def multiply(x):
    return x * 2

def apply_twice(f, x):
    return f(f(x))

r = apply_twice(multiply, 8)
print(r)

