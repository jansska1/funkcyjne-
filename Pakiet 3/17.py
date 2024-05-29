def capitalize_all_words(s):
    return ' '.join(word.capitalize() for word in s.split())

example_string = "hello world"
capitalized = capitalize_all_words(example_string)
print("Capitalized words:", capitalized)