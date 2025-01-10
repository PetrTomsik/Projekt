from predmet import Predmet

class Lokace:
    def __init__(self, jmeno, predmety):
        self.jmeno = jmeno
        self.predmety = predmety

    def aktualizuj_ceny(self):
        for predmet in self.predmety:
            predmet.aktualizuj_cenu()