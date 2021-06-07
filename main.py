print("Welkom bij galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

print(" ")

import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Het woord heeft "+ str(lengtewoord) + " letters...")

print(" ")

print("Je hebt 5 beurten, typ een letter en we beginnen!")

beurten = 5

print(" ")

userinput = input("Typ hier je letter: ")
gekozenletters = userinput

lijst = []
lijst.append(userinput)

for letter in woord:
  if letter in gekozenletters:
    print(letter)
  else:
    print("_")

if userinput in woord:
  print(" ")
  print("Gefeliciteerd deze letter zit in het woord!")
if userinput not in woord:
  print(" ") 
  print("Jammer deze letter zit niet in het woord :(")