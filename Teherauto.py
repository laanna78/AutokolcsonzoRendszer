from Auto import Auto

class Teherauto(Auto):
    def __init__(self, reg_number: str, brand: str, max_weight: int, rental_price: int):
        super().__init__(reg_number, brand, rental_price)
        self.max_weight = max_weight

    def specific_data(self):
        return f"Teherautó, max. össztömeg: {self.max_weight} tonna"