def most_frequent(lst):
    from collections import Counter
    counter = Counter(lst)
    return counter.most_common(1)[0][0]

example_list = [1, 3, 2, 1, 2, 1, 3, 3, 3]
most_freq = most_frequent(example_list)
print("Most frequent element:", most_freq)