
class decors:
    
    @staticmethod
    def log_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("log")
            return result
        return wrapper
    
    @staticmethod
    def sir_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print("siri")
            return result
        return wrapper

class Calculator:

    @decors.log_decorator
    def add(self, a, b):
        return a + b

    @decors.sir_decorator
    def add2(self, a, b):
        return a + b

# Example usage
calc = Calculator()
calc.add(5, 3)
calc.add2(5, 3)
