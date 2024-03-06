def lazy_loading(x):
    for i in range(x):
        yield i * 2

for value in lazy_loading(5):
    print(value)