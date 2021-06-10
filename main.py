print("Welkom bij Galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

print(" ")

import random

counter = 0
woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

woord = random.choice(woordenlijst)
lengtewoord = len(woord)

print("Het woord heeft "+ str(lengtewoord) + " letters...")

print(" ")

print("Je hebt 6 beurten, typ een letter en we beginnen!")

print(" ")

userinput = input("Typ hier je letter: ")
gekozenletters = userinput

print(" ")

for letter in woord:
  if letter in gekozenletters:
    print(letter,end=' ')
  else:
    print("_ ",end='')

if userinput in woord:
  print(" ")
  print(" ")
  print("Gefeliciteerd deze letter zit in het woord!")
if userinput not in woord:
  print(" ")
  print(" ")
  print("Jammer deze letter zit niet in het woord :(") 
  counter = counter + 1
  if counter == 1:
      print("""  
      |
      |
      |
      |
      |
 _____|""")
  elif counter == 2:
           print("""  ____
      |
      |
      |
      |
      |
 _____|""")
  elif counter == 3:
            print("""  ____
     \|
      |
      |
      |
      |
 _____|""")
  elif counter == 4:
      print("""  ____
   | \|
      |
      |
      |
      |
 _____|""")
  elif counter == 5:
      print("""  ____
   | \|
   0  |
      |
      |
      | 
 _____|""")
  elif counter == 6:
      print("""  ____
   | \|
   0  |
   |  |
      |
      |
 _____|""")
  elif counter == 7:
      print("""  ____
   | \|
   0  |
  /|  |
      |
      |
 _____|""")
  elif counter == 8:
      print("""  ____
   | \|
   0  |
  /|\ |
      |
      |
 _____|""")
  elif counter == 9:
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

print(" ")
print("Het woord was "+ str(woord) +"!")
      

lijst = []
lijst.append(userinput)

if lijst is woord:
  print("Gefeliciteerd! Je hebt het woord geraden!")
