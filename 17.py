from functools import partial

def fnc(x, y):
    return x + y

added = partial(fnc, 3)

print(added(3))