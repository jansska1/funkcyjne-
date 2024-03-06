names_list = ['Albert', 'Iza', "Franek", 'Rafał', "Aga", 'Ela', 'Magda']

result = list(filter(lambda name: len(name) > 4, names_list))

print(result)
