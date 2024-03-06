def make_multiplier(x):
    def multiply(y):
        return x * y
    return multiply

r = make_multiplier(3)(3)
print(r)