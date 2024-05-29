def generate_permutations(lst):
    from itertools import permutations
    return list(permutations(lst))

example_list = [1, 2, 3]
permutations = generate_permutations(example_list)
print("Permutations:", permutations)