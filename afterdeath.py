import atexit
import time

def first_cleanup():
    print("First cleanup...")

def second_cleanup():
    print("Second cleanup...")
    
print("Program is running. 1")

# Register functions
atexit.register(first_cleanup)
atexit.register(second_cleanup)

print("Program is running. 2")

# Simulate some processing
time.sleep(2)  # Sleep for 2 seconds to simulate work

print("Program is ending.")
