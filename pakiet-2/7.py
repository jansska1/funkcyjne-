import itertools

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

sorted_data = sorted(data, key=lambda x: x % 2)

for key, group in itertools.groupby(sorted_data, key=lambda x: 'parzyste' if x % 2 == 0 else 'nieparzyste'):
    print(key, list(group))

