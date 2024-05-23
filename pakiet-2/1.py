from itertools import product

iterbales = [['A', 'B'], ['C', 'D']]

result = list(product(*iterbales))
print (result)


