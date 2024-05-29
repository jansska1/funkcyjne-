def chunk_list(lst, max_length):
    return [lst[i:i + max_length] for i in range(0, len(lst), max_length)]

example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunked = chunk_list(example_list, 3)
print("Chunked list:", chunked)