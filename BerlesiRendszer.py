from Szemelyauto import Szemelyauto
from Teherauto import Teherauto
from Autokolcsonzo import Autokolcsonzo
from Berles import Berles
from datetime import datetime

class RentACar:
    def __init__(self):
        self._autokolcsonzo = Autokolcsonzo("Verdák")
        self._cars_to_rent()
        self._rental_list()

    def _cars_to_rent(self):
        self._autokolcsonzo.add_auto(Szemelyauto("ABC123", "Nissan", 5, 8000))
        self._autokolcsonzo.add_auto(Szemelyauto("XYZ456", "Volvo", 7, 12000))
        self._autokolcsonzo.add_auto(Teherauto("TIR789", "Scania", 24, 35000))

    def _rental_list(self):
        self._autokolcsonzo.add_berles(Berles(self._autokolcsonzo.autok[0], datetime(2024, 10, 31)))
        self._autokolcsonzo.add_berles(Berles(self._autokolcsonzo.autok[1], datetime(2024, 10, 31)))
        self._autokolcsonzo.add_berles(Berles(self._autokolcsonzo.autok[1], datetime(2024, 11, 1)))
        self._autokolcsonzo.add_berles(Berles(self._autokolcsonzo.autok[2], datetime(2024, 10, 31)))

    def rent_by_reg_number(self):
        reg_number = input("Add meg a jármű rendszámát, amit szeretnél kibérelni: ")
        for auto in self._autokolcsonzo.autok:
            if auto.reg_number == reg_number:
                date = input("Add meg a bérlés napját (ÉÉÉÉ-HH-NN): ")
                try:
                    date = datetime.strptime(date, "%Y-%m-%d")

                    for berles in self._autokolcsonzo.berlesek:
                        if berles.auto == auto and berles.date == date:
                            print(
                                f"HIBA: A(z) {auto.reg_number} rendszámú {auto.brand} már ki van bérelve erre a napra!")
                            return

                    berles = Berles(auto, date)
                    self._autokolcsonzo.berlesek.append(berles)
                    auto.available = False
                    print(f"A(z) {auto.reg_number} rendszámú {auto.brand} sikeresen kibérelve! Fizetendő: {auto.rental_price} huf/nap")
                    return
                except ValueError:
                    print("Érvénytelen dátum formátum.")
                return
        print("Nincs ilyen rendszámú autó.")

    def return_by_reg_number(self):
        reg_number = input("Add meg a jármű rendszámát, amit szeretnél lemondani: ")
        for auto in self._autokolcsonzo.autok:
            if auto.reg_number == reg_number:
                date = input("Add meg a lemondás napját (ÉÉÉÉ-HH-NN): ")
                try:
                    date = datetime.strptime(date, "%Y-%m-%d")
                    lemondas = Berles(auto, date)
                    for berles in self._autokolcsonzo.berlesek:
                        if berles == lemondas:
                            self._autokolcsonzo.berlesek.remove(lemondas)
                            auto.available = True
                            print(f"A(z) {auto.reg_number} rendszámú {auto.brand} sikeresen lemondva!")
                        else:
                            print(f"Nincs ilyen dátummal érvényes bérlés a(z) {auto.reg_number} rendszámú {auto.brand} járműre!")
                        return
                except ValueError:
                    print("Érvénytelen dátum formátum.")
                return

        print("Nincs ilyen rendszámú autó.")


    def user_interact(self):
        while True:
            print("1. Járművek listázása")
            print("2. Bérlések listázása")
            print("3. Jármű bérlés")
            print("4. Jármű lemondás")
            print("5. Kilépés")

            try:
                choice = int(input("Válassz a fenti menüpontok közül: "))

                while choice < 1 or choice > 5:
                    choice = int(input("1 és 5 közötti számot válassz: "))

                if choice == 1:
                    self._autokolcsonzo.display_autok()
                elif choice == 2:
                    self._autokolcsonzo.display_berlesek()
                elif choice == 3:
                    self.rent_by_reg_number()
                elif choice == 4:
                    self.return_by_reg_number()
                elif choice == 5:
                    break

            except ValueError:
                print("Csak számot adhatsz meg: 1 és 5 közötti számot válassz!")


autokolcsonzo = RentACar()
autokolcsonzo.user_interact()