from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str

# Creating an instance of the Person dataclass
person = Person(name="Alice", age=30, city="New York")

print(person)  # Output: Person(name='Alice', age=30, city='New York')
print(person.name)  # Output: Alice
