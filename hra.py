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
        print(f"Maximum předmětů: {hrac.max_velikost_inventare}")
        for i, misto in enumerate(lokace):
            print(f"{i+1}. {misto.jmeno}")

        vyber = int(input("Cesta ?")) - 1
        aktualni_lokace = lokace[vyber]
        dny += 1

        if aktualni_lokace.jmeno == "Večerka":
            rozsireni = input("Chcete koupit kabát (150Kč) nebo batoh (400Kč)? ").strip().lower()
            hrac.rozsirit_inventar(rozsireni)
        else:
            aktualni_lokace.aktualizuj_ceny()
            print(f"Vítej v {aktualni_lokace.jmeno}")
            for predmet in aktualni_lokace.predmety:
                print(f"{predmet.jmeno}: {predmet.aktualni_cena} Kč")
            akce = input(f"Co cheš dělat? (1 - Prodat / 2 - Koupit)")

            if akce == '1':
                nazev_predmetu  = input(f"Co chceš prodat? ")
                aktualni_lokace.prodat_predmet(nazev_predmetu, hrac)
            elif akce == '2':
                nazev_predmetu = input("Co chceš koupit? ")
                aktualni_lokace.koupit_predmet(nazev_predmetu, hrac)

    print(f"\nHra skončila. Zbylo Vám {hrac.penize} Kč.")
    with open("highscores.txt", "a") as file:
        file.write(f"{hrac.jmeno}: {hrac.penize} Kč\n")
    print("Žebříček:")
    with open("highscores.txt", "r") as file:
        print(file.read())



if __name__ == "__main__":
    main()