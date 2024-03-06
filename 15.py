def add(a, b):
    return a + b

def add_curried(a):
    def sum(b):
        return add(a, b)
    return sum

print(add_curried(2)(3))