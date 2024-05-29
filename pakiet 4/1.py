def sum_even_numbers(lst):
    return sum(x for x in lst if x % 2 == 0)

example_list = [1, 2, 3, 4, 5, 6]
sum_evens = sum_even_numbers(example_list)
print("Sum of even numbers:", sum_evens)

