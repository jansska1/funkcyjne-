y = 5
def incrementorPublic(x):
    x = 5
    return lambda x: x * y

result = incrementorPublic(10)
print(result(10))
