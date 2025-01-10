import random

class Predmet:
    def __init__(self, jmeno, min_cena, max_cena):
        self.jmeno = jmeno
        self.min_cena = min_cena
        self.max_cena = max_cena
        self.aktualni_cena = random.randint(self.min_cena, self.max_cena)

    def aktualizuj_cenu(self):
        zmena = random.randint(-5, 5)
        self.aktualni_cena = max(self.min_cena, min(self.max_cena, self.aktualni_cena + zmena))