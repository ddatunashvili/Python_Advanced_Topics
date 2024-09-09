

# not need to create an object 
# no need to use self
# can coexist in classes

class MathUtils:
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

# Calling static method without creating an instance
print(MathUtils.add(5, 3)) 

