import time
import functools

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper
@timeit
def example_func(n):
    result = 0
    for i in range(n):
        result += i
    return result

# Wywołanie ozdobionej funkcji
example_func(1000000)