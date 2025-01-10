
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

    def rozsirit_inventar(self, typ_rozsireni):
        if typ_rozsireni == "kabát" and self.penize >= 150:
            self.penize -= 150
            self.max_velikost_inventare += 2
            print("Koupili jste kabát. Inventář rozšířen o 2 místa.")
        elif typ_rozsireni == "batoh" and self.penize >= 400:
            self.penize -= 400
            self.max_velikost_inventare += 3
            print("Koupili jste batoh. Inventář rozšířen o 3 místa.")
        else:
            print("Nemáte dost peněz.")