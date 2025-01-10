from hrac import Hrac
from lokace import Lokace
from predmet import Predmet
import random

def main():
    #Inicializace
    predmety = [
        Predmet("Utopenec", 50, 100),
        Predmet("Med", 100, 200),
        Predmet("Láhev pálavy", 200, 500)
    ]
    lokace = [
        Lokace("Hradčany", predmety),
        Lokace("Václavák", predmety),
        Lokace("Holešovice", predmety),
        Lokace("Večerka", [])
    ]
    hrac = Hrac(input("Zadej jméno: "))

    dny = 0
    while dny < 14:
        print(f"\n{dny}/14 dnů - Lokace: {lokace[0].jmeno}")
        print(f"Peníze: {hrac.penize} Kč, Inventář: {[predmet.jmeno for predmet in hrac.inventar]}")
        for i, misto in enumerate(lokace):
            print(f"{i+1}. {misto.jmeno}")

        vyber = int(input("Cesta ?")) - 1
        aktualni_lokace = lokace[vyber]
        dny += 1
        aktualni_lokace.aktualizuj_ceny()
        print(f"Výtej v {aktualni_lokace.jmeno}")
        for predmet in aktualni_lokace.predmety:
            print(f"{predmet.jmeno}: {predmet.aktualni_cena} Kč")
        akce = int(input(f"Co cheš dělat? (1 - Prodat / 2 - Koupit)"))
        if akce == 1:
            nazev_predmetu  = input(f"Co chceš prodat?")
            #aktualni_lokace.




