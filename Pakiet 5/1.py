nameList = ["Bodzio", "Adam", "Szymek"]

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