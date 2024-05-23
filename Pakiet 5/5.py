arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def list(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(arr[i])

x = lambda a, b : a * b

list(arr)
print(x(5, 5))