from predmet import Predmet

class Lokace:
    def __init__(self, jmeno, predmety):
        self.jmeno = jmeno
        self.predmety = predmety

    def aktualizuj_ceny(self):
        for predmet in self.predmety:
            predmet.aktualizuj_cenu()

    def koupit_predmet(self, jmeno_predmetu, hrac):
        for predmet in self.predmety:
            if predmet.jmeno == jmeno_predmetu and hrac.penize >= predmet.aktualni_cena:
                hrac.koupit(predmet, predmet.aktualni_cena)
                return
        print("Nemáš dost peněz.")

    def prodat_predmet(self, jmeno_predmetu, hrac):
        for predmet in self.predmety:
            if predmet.jmeno == jmeno_predmetu and predmet in hrac.inventar:
                hrac.prodat(predmet, predmet.aktualni_cena)
                return
        print("Nemáš tento předmět v inventáři.")