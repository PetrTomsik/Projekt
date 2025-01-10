from predmet import Predmet

class Lokace:
    def __init__(self, jmeno, predmety):
        self.jmeno = jmeno
        self.predmety = [Predmet(predmet.jmeno, predmet.min_cena, predmet.max_cena) for predmet in predmety]

    def aktualizuj_ceny(self):
        for predmet in self.predmety:
            predmet.aktualizuj_cenu()

    def koupit_predmet(self, jmeno_predmetu, hrac):
        for predmet in self.predmety:
            if predmet.jmeno == jmeno_predmetu and hrac.penize >= predmet.aktualni_cena:
                if len(hrac.inventar) < hrac.max_velikost_inventare:
                    hrac.koupit(predmet, predmet.aktualni_cena)
                else:
                    print("Není místo v inventáři.")
                return
        print("Nemáš dost peněz.")

    def prodat_predmet(self, jmeno_predmetu, hrac):
        for predmet in hrac.inventar:
            if predmet.jmeno == jmeno_predmetu:
                for predmet_lokace in self.predmety:
                    if predmet_lokace.jmeno == jmeno_predmetu:
                        hrac.prodat(predmet, predmet_lokace.aktualni_cena)
                        return
        print("Nemáte tento předmět k prodeji.")