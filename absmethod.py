

from abc import ABC, abstractmethod

# Abstract Base Classes 
# checks if children has same method and property
class PaymentProcessor(ABC):
    
    # check if subclas has method and returning None
    @abstractmethod
    def process_payment(self) -> None:
        pass
    
    # checks if subclass has property of amount defined as method 
    @property
    @abstractmethod
    def amount(self):
        pass
    
    # checks if subclass has setter and it has argument as float
    @amount.setter
    @abstractmethod
    def amount(self, new)-> int:
        pass

class CreditCardPayment(PaymentProcessor):
    
    def __init__(self, amount):
        self.__amount = amount
        
    def process_payment(self):
        return self.amount
    
    # Getter
    @property
    def amount(self):
        return self.__amount
    
    # deleter
    @amount.deleter
    def amount(self):
        del self.__amount
        
    # setter
    @amount.setter
    def amount(self, other):
        self.__amount = other
        print(self.__amount)
        
    # Read-Only Property (computed property)
    @property
    def is_positive(self):
        return self.__amount > 0
    


        
credit_card = CreditCardPayment(100)


# credit_card.process_payment()

# print(credit_card.is_positive)

credit_card.amount = 20.0


