from osoba import Osoba
from lokace import Lokace
from predmet import Predmet
import random

def main():
    predmety = [
        Predmet("Utopenec", 50, 100),
        Predmet("Med", 100, 200),
        Predmet("Láhev pálavy", 200, 500)
    ]
    lokace = [
        Lokace("Hradčany", predmety),
        Lokace("Václavák", predmety),
        Lokace("Holešovice", predmety)
    ]
    osoba = Osoba(input("Zadej jméno: "))

    dny = 0
    while dny < 14:
        print(f"Peníze: {osoba.money} Kč, Inventář: {[predmet.jmeno for predmet in osoba.inventar]}")
        print(f"\n{dny}/14 dnů - Lokace: {lokace[0].name}")