def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'error {e}')
            return None
    return wrapper

@safe_function
def dividing(x, y):
    x / y
    pass

dividing(2, 0)
