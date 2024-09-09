from dataclasses import dataclass, field

@dataclass
class Car:
    make: str
    model: str
    year: int = 2020  # Default value
    owners: list = field(default_factory=list)  # Default factory

# Creating a Car instance
car = Car(make="Toyota", model="Corolla")
car.owners.append("Alice")
print(car)  # Output: Car(make='Toyota', model='Corolla', year=2020, owners=['Alice'])

            
# -----------------------------------------------------

@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height

rect = Rectangle(3.0, 4.0)
print(rect.area())  # Output: 12.0

# -----------------------------------------------------

# modify classes
class Meta(type):
    def __new__(self, class_name, bases, attrs):
        
        attrs={i.upper() if not i.startswith("__") else i:v for i,v in attrs.items()}
        print(attrs)
        return type(class_name, bases, attrs)
        
class Dog(metaclass=Meta):
    y = 5
    x = 8
    
# -----------------------------------------------------
