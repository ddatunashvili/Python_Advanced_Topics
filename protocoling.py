from typing import Protocol

# Protocols
# protocols are used when using type aliases
# procols can check return types and required methos (structure)
# mypy protocoling.py

class Flyable(Protocol):
    @property
    def altitude(self) -> int:
        pass

    @property
    def speed(self) -> int:
        pass
    
    def reqired(self) -> None:
        pass

class Airplane:
    def __init__(self, altitude: int, speed: int):
        self._altitude = altitude
        self._speed = speed
        
    @property
    def altitude(self) -> int:
        return self._altitude
    
    @property
    def speed(self) -> None:
        return 

def perform_flight_operations(flyable: Flyable) -> None:
    print(flyable.altitude)

# Instantiate Airplane with the required arguments
airplane = Airplane(30000, 600)

perform_flight_operations(airplane)
