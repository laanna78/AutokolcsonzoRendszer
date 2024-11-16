class Berles:
    def __init__(self, auto, date):
        self.auto = auto
        self.date = date

    def __eq__(self, other):
        return isinstance(other, Berles) and self.auto == other.auto and self.date == other.date