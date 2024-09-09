
# can create instances inside class
# change class level vars or add 
# can alternate (alter) constructor

class Person:
    # Class level variable to count instances
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")
    
    # i can run it without creating person class and it will create person
    @classmethod
    def from_title(cls, name):
        return cls(name, "Unknown")


person1 = Person("Alice")
person2 = Person.create_anonymous() # (alter) constructor

print(person1.name)       
print(person2.name)        

# change class level vars or add 
print(Person.get_population())  



