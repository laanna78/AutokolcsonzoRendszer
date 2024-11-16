from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, reg_number: str, brand: str, rental_price: int):
        self.reg_number = reg_number
        self.brand = brand
        self.rental_price = rental_price
        self.available = True

    @abstractmethod
    def specific_data(self):
        pass
