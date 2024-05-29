def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_generator = generate_fibonacci()

for _ in range(10):
    print(next(fib_generator))