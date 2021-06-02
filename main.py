print("Welkom bij galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

print(" ")

import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

woord = random.choice(woordenlijst)
lengtewoord = len(woord)
streepjes = '_ ' * len(woord)

print("Het woord heeft "+ str(lengtewoord) + " letters...")

print(" ")

print("Je hebt 5 beurten, typ een letter en we beginnen!")

beurten = 5

print(" ")

print(streepjes)
