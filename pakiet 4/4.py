def exponentiate_factory(exponent):
    return lambda x: x ** exponent

square = exponentiate_factory(2)
cubed = exponentiate_factory(3)
print("Square of 3:", square(3))
print("Cube of 2:", cubed(2))