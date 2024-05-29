string_list = ["hello", "world", "Python", "is", "awesome"]

def filter_long_words(words):
    avg = len(''.join(words)) / len(words)
    return filter(lambda word: len(word) > avg, words)

print(list(filter_long_words(string_list)))
