list = ['adam', 'ada', 'adamowo', 'adamy', ]

def sort(n):
  return sorted(n, key=lambda word: len(word))

result = sort(list)

print(result)
