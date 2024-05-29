def partition_list(lst, condition):
    true_list = []
    false_list = []
    for item in lst:
        if condition(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return true_list, false_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_condition = lambda x: x % 2 == 0
evens, odds = partition_list(numbers, even_condition)
print("Even numbers:", evens)
print("Odd numbers:", odds)