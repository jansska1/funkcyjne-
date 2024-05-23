def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

result = fibonacci()

for i in range(10):
    print(next(result))

with open('plik.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()