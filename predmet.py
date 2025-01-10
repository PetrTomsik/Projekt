import random

class Predmet:
    def __init__(self, jmeno, min_cena, max_cena):
        self.jmeno = jmeno
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.aktualni_cena = random.randint(self.min_cena, self.max_cena)

    def aktualizuj_cenu(self):
        znema = random.randint(-5, 5)
        self.aktualni_cena += znema

