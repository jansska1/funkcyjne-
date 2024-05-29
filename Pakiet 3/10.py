def cumulative_sum(lst):
    result = []
    total = 0
    for num in lst:
        total += num
        result.append(total)
    return result

example_list = [1, 2, 3, 4, 5]
cumulative = cumulative_sum(example_list)
print("Cumulative sum:", cumulative)