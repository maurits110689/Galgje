import random
import re

def spel():

 print("Welkom bij Galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")

 print(" ")
 a = "Veel "
 b = "plezier!"
 c = a + b
 print(c)

 print(" ")

 counter = 10
 woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

 woord = random.choice(woordenlijst)
 lengtewoord = len(woord)
 temp = "_ " * lengtewoord

 print("Het woord heeft "+ str(lengtewoord) + " letters...")

 print(" ")

 print("Je hebt 10 beurten, typ een letter en we beginnen!")

 print(" ")

 while True:
   userinput = input("Typ hier je letter: ")
   userinput = userinput.lower()
   gekozenletters = userinput
   x = userinput.isalpha()
   if x is False:
    print(" ")
    print("Oeps, je hebt iets anders dan een letter ingevuld probeer het opnieuw!")
    print(" ")
    counter = counter - 1
    if counter == 1:
      print("Je hebt nog "+ str(counter)+ " beurt!")
      print(" ")
    if counter == 0:
      print("Jammer, je hebt verloren het woord was " + str(woord) + "!")
      again = input("Wil je nog een keer spelen? ja of nee? ")
      if again == "ja" or again == "Ja":
         print(" ")
         spel()
      else:
         print("Tot ziens! :)")
         quit()
    if counter > 1:
      print("Je hebt nog "+ str(counter)+ " beurten!")
      print(" ")
      pass
   match = re.search(userinput, woord)
   if userinput == woord:
      print("Gefeliciteerd! Je heb het woord " + str(woord) + " geraden!")

      again = input("Wil je nog een keer spelen? ja of nee? ")
      if again == "ja" or again == "Ja":
         print(" ")
         spel()
      else:
         print("Tot ziens! :)")
         quit()

   elif userinput in woord:
    print(" ")
    print("Gefeliciteerd deze letter zit in het woord!")
    print(" ")
    for i in range(0, lengtewoord):
       if userinput == woord [i]:
         temp = temp[:i] + userinput + temp[i+1:]
         print(temp)
    print(" ")

   else:
    if x is True:
      print(" ")
      print("Jammer deze letter zit niet in het woord : (")
      counter = counter - 1
      if counter == 9:
        print(" ")
        print("Je hebt nog 9 beurten!")
        print("""  
     |
     |
     |
     |
     |
_____|
""")
      elif counter == 8:
             print(" ")
             print("Je hebt nog 8 beurten!")
             print("""  ____
     |
     |
     |
     |
     |
_____|
""")
      elif counter == 7:
              print(" ")
              print("Je hebt nog 7 beurten!")
              print("""  ____
    \|
     |
     |
     |
     |
_____|
""")
      elif counter == 6:
        print(" ")
        print("Je hebt nog 6 beurten!")
        print("""  ____
  | \|
     |
     |
     |
     |
_____|
""")
      elif counter == 5:
        print(" ")
        print("Je hebt nog 5 beurten!")
        print("""  ____
  | \|
  0  |
     |
     |
     |
_____|
""")
      elif counter == 4:
        print(" ")
        print("Je hebt nog 4 beurten!")
        print("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|
""")
      elif counter == 3:
        print(" ")
        print("Je hebt nog 3 beurten!")
        print("""  ____
  | \|
  0  |
 /|  |
     |
     |
_____|
""")
      elif counter == 2:
       print(" ")
       print("Je hebt nog 2 beurten!")
       print("""  ____
  | \|
  0  |
 /|\ |
     |
     |
_____|
""")
      elif counter == 1:
        print(" ")
        print("Je hebt nog 1 beurt!")
        print("""  ____
  | \|
  0  |
 -|- |
 /   |
     |
_____|
""")
      elif counter == 0:
       print(" ")
       print("Helaas, je bent dood!")
       print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|
""")
       print(" ")
       print("Jammer, je hebt verloren het woord was " + str(woord) + "!")
       again = input("Wil je nog een keer spelen? ja of nee? ")
       if again == "ja" or again == "Ja":
         print(" ")
         spel()
       else: 
         print("Tot ziens! :)")
         quit()


spel()