# program-1: Find only one card, neigher king not spades from the deck
cards = 52
kings = 4
shades = 13
kingsAndShades = 1

totalKingsShades = shades + kings - kingsAndShades

choosenCard = cards - totalKingsShades

possibility = choosenCard/cards

print("*********************************************************************")
print(f"Possibility of neighter king not spades is {possibility:.4f}")
print("*********************************************************************")