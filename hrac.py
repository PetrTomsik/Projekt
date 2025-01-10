
class Hrac:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.penize = 100
        self.inventar = []
        self.max_velikost_inventare = 2

    def prodat(self, predmet, cena):
        self.penize += cena
        self.inventar.remove(predmet)
        print(f"Prodal si {predmet.jmeno} za {cena} Kč")


    def koupit(self, predmet, cena):
        self.penize -= cena
        self.inventar.append(predmet)
        print(f"Koupil si {predmet.jmeno} za {cena} Kč")