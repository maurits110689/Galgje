print("Welkom bij Galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

print(" ")

import random

counter = 0
woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Het woord heeft "+ str(lengtewoord) + " letters...")

print(" ")

print("Je hebt 10 beurten, typ een letter en we beginnen!")

print(" ")

userinput = input("Typ hier je letter: ")
gekozenletters = userinput
x = userinput.isalpha()
if x is False:
 print(" ")
 print("Oeps, je hebt iets anders dan een letter ingevuld probeer het opnieuw!")

if userinput in woord:
  print(" ")
  for letter in woord:
   if letter in userinput:
     print(letter,end=' ')
   else:
     print("_",end=' ')
  print("")
  print("")
  print("Gefeliciteerd deze letter zit in het woord!")
if userinput not in woord:
  if x is True:
    print(" ")
    print("Jammer deze letter zit niet in het woord :(")
    counter = counter + 1
    if counter == 1:
      print(" ")
      print("Je hebt nog 9 beurten!")
      print("""
      |
      |
      |
      |
      |
 _____|""")
    elif counter == 2:
           print(" ")
           print("Je hebt nog 8 beurten!")
           print("""  ____
      |
      |
      |
      |
      |
 _____|""")
    elif counter == 3:
            print(" ")
            print("Je hebt nog 7 beurten!")
            print("""  ____
     \|
      |
      |
      |
      |
 _____|""")
    elif counter == 4:
      print(" ")
      print("Je hebt nog 6 beurten!")
      print("""  ____
   | \|
      |
      |
      |
      |
 _____|""")
    elif counter == 5:
      print(" ")
      print("Je hebt nog 5 beurten!")
      print("""  ____
   | \|
   0  |
      |
      |
      | 
 _____|""")
    elif counter == 6:
      print(" ")
      print("Je hebt nog 4 beurten!")
      print("""  ____
   | \|
   0  |
   |  |
      |
      |
 _____|""")
    elif counter == 7:
      print(" ")
      print("Je hebt nog 3 beurten!")
      print("""  ____
   | \|
   0  |
  /|  |
      |
      |
 _____|""")
    elif counter == 8:
      print(" ")
      print("Je hebt nog 2 beurten!")
      print("""  ____
   | \|
   0  |
  /|\ |
      |
      |
 _____|""")
    elif counter == 9:
      print(" ")
      print("Je hebt nog 1 beurt!")
      print("""  ____
   | \|
   0  |
  -|- |
  /   |
      |
 _____|""")
    elif counter ==10:
      print("Helaas, je bent dood")
      print("""  ____
   | \|
   0  |
  -|- |
  / \ |
      |
 _____|""")

if counter == 10:
 print(" ")
 print("Het woord was "+ str(woord) +"!")
      
lijst = []
lijst.append(userinput)

if lijst is woord:
  print("Gefeliciteerd! Je hebt het woord geraden!")
