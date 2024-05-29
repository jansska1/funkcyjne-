def split_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
splitted = split_list(example_list, 3)
print("Split list:", splitted)