def remove_whitespace(lst):
    return [s.strip() for s in lst]

example_list = ['  apple  ', '  banana  ', 'cherry  ']
no_whitespace = remove_whitespace(example_list)
print("No whitespace:", no_whitespace)