from functools import wraps



def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Using the decorated function
result = add(5, 3)
print(f"Function name: {add.__name__}")
print(f"Function docstring: {add.__doc__}")
