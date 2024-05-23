numbers = [1,2,3,4,5,6,7]
squared = [num ** 2 for num in numbers if (square := num ** 2) > 10]

print(squared)