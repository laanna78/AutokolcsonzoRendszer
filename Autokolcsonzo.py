class Autokolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []
        self._berlesek = []

    @property
    def name(self):
        return self._name

    @property
    def autok(self):
        return self._autok

    def add_auto(self, new_auto):
        self._autok.append(new_auto)

    @property
    def berlesek(self):
        return self._berlesek

    def add_berles(self, new_berles):
        self._berlesek.append(new_berles)

    def display_autok(self):
        for auto in self.autok:
            print(f"{auto.specific_data()}. Rendszám: {auto.reg_number}, Típus: {auto.brand}, Bérleti díj: {auto.rental_price} huf/nap, Elérhető-e: {auto.available}")

    def display_berlesek(self):
        for berles in self.berlesek:
            print(f"{berles.auto.reg_number} rendszámú {berles.auto.brand} jármű erre a napra kibérelve: {berles.date}. Fizetendő: {berles.auto.rental_price}")
