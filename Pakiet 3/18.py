def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

example_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(example_matrix)
print("Transposed matrix:", transposed)