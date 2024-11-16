from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, reg_number: str, brand: str, number_of_seats: int, rental_price: int):
        super().__init__(reg_number, brand, rental_price)
        self.number_of_seats = number_of_seats

    def specific_data(self):
        return f"Személyautó, ülőhely: {self.number_of_seats} db"