def sum_of_squares_of_odds(lst):
    return sum(x**2 if x % 2 != 0 else 0 for x in lst)

example_list = [1, 2, 3, 4, 5]
sum_squares_odds = sum_of_squares_of_odds(example_list)
print("Sum of squares of odds:", sum_squares_odds)