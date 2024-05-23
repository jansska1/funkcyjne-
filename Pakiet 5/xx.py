from f2 import printin
import math

nameList = ["Bodzio", "Adam", "Szymek"]
wordsList = ['autokar', 'okno', 'auto', 'kusza', 'armia', 'odlew']
arr = [1, 2, 3, 4, 5, 6, 7, 8]
y = 5

#1

print("funkcja predefiniowana")

for i in range(len(nameList)):
    print(nameList[i])

def incrementor(x):
    y = 3
    return lambda x: x * y

num = -5
print(abs(num))

result = incrementor(10)
print(result(10))

#2

printin()

#3

def incrementorPublic(x):
    x = 5
    return lambda x: x * y

result = incrementorPublic(10)
print(result(10))

#4
def add(a, b):
    return a + b

def sum(f, a, b):
    return f(a,b)

r = sum(add, 2, 5)
print(r)

#5

def list(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            print(arr[i])

x = lambda a : pow(a, 2)

list(arr)
print(x(5))

#6

def checkA(wordsList):
    if wordsList[0] == "a":
        return True
    return False

def out(f):
    for x in f:
        print(x)

filtered = filter(checkA, wordsList)

out(filtered)

#7.py







