print("Welkom bij Galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

print(" ")

import random

woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Het woord heeft "+ str(lengtewoord) + " letters...")

print(" ")

print("Je hebt 5 beurten, typ een letter en we beginnen!")

x = "6"

print(" ")

userinput = input("Typ hier je letter: ")
gekozenletters = userinput

print(" ")

lijst = []
lijst.append(userinput)

for letter in woord:
  if letter in gekozenletters:
    print(letter,end=' ')
  else:
    print("_ ",end='')

print(" ")

if userinput in woord:
  print(" ")
  print("Gefeliciteerd deze letter zit in het woord!")
if userinput not in woord:
  print(" ") 
  print("Jammer deze letter zit niet in het woord :(") 
  pogingen = x
  print(" ")
  print("Je hebt nog " + str(pogingen) + " pogingen!")


def drawgalgjes():
   if pogingen == 5:
        print("Jammer, je hebt nog 4 pogingen over")
        print("""     ____
      | \|
      o  |
         |
         |
         |
    _____|""")
   if pogingen == 4:
        print("Jammer, je hebt nog 3 pogingen over")
        print("""     ____
      | \|
      o  |
      |  |
         |
         |
    _____|""")
   if pogingen == 3:
        print("Jammer, je hebt nog 2 pogingen over")
        print("""     ____
      | \|
      o  |
     /|\ |
         |
         |
    _____|""")

   if pogingen == 2:
        print("je hebt nog 1 pogingen over")
        print("""     ____
      | \|
      o  |
     /|\ |
     / \ |
         |
    _____|""")

   if pogingen == 1:
        print("""     ____
      | \|
      o  |
     /|\ |
     / \ |
         |
    _____|""")