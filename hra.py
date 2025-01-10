from hrac import Hrac
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
    hrac = Hrac(input("Zadej jméno: "))

    dny = 0
    while dny < 14:
        print(f"Peníze: {hrac.penize} Kč, Inventář: {[predmet.jmeno for predmet in hrac.inventar]}")
        print(f"\n{dny}/14 dnů - Lokace: {lokace[0].jmeno}")