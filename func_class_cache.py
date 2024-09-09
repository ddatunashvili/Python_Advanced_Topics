import time
from functools import lru_cache




# With caching
@lru_cache(maxsize=128)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

# Measure time for the cached version (be cautious with large values)
try:
    start_time = time.time()
    print("Fibonacci with caching (n=300):", fib_with_cache(300))  # Use a smaller value for testing
    print("Time taken with caching:", time.time() - start_time)
except RecursionError as e:
    print("RecursionError:", e)
    
    
from functools import cached_property

class MyClass:
    @cached_property
    def expensive_computation(self):
        # Simulate an expensive computation
        return sum(range(1000))

obj = MyClass()
print(obj.expensive_computation)  # Computed once and cached




from functools import cache

@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Using the cached function
print(factorial(5))  # Output: 120