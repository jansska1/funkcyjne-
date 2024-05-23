import inspect

avg = lambda x, y, z: (x + y + z) / len(inspect.signature(avg).parameters)

print(avg(3,3,3))