#toestaan gebruik van de random module
import random
#toestaan gebruik van de re module
import re
#begin functie spel/gameloop
def spel():
#welkomsbericht
 print("Welkom bij Galgje! Je moet het geheime woord raden voordat je pogingen op zijn!")
#string concatenation
 print(" ")
 a = "Veel "
 b = "plezier!"
 c = a + b
 print(c)
 print(" ")
#beurten en woordenlijst en gebruikte letters
 counter = 10
 woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
 gebruikteletters = []
#random woord kiezen en lengte woord en streepjes bepalen
 woord = random.choice(woordenlijst)
 lengtewoord = len(woord)
 temp = "-" * lengtewoord
#aantal letters weergeven
 print("Het woord heeft "+ str(lengtewoord) + " letters...")

 print(" ")
#begin en beurten weergeven
 print("Je hebt 10 beurten, typ een letter en we beginnen!")

 print(" ")
#while loop
 while True:
#letter vragen
   userinput = input("Typ hier je letter: ")
   userinput = userinput.lower()
   gekozenletters = userinput
   x = userinput.isalpha()
   match = re.search(userinput, woord)
#error bericht twee karakters
   if len(gekozenletters) > 1:
     print(" ")
     print("Oeps, je hebt twee dingen ingevuld! Probeer het opnieuw!")
     print(" ")
     counter = counter - 1
#beurten - aantal voor error twee karakters en opnieuw spelen optie wanneer de beurten opzijn
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
     continue
#error bericht non alfabetische input
   if x is False:
    print(" ")
    print("Oeps, je hebt iets anders dan een letter ingevuld probeer het opnieuw!")
    print(" ")
    counter = counter - 1
#beurten - aantal voor error non alfabetische input en opnieuw spelen optie wanneer de beurten opzijn
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
#felicitatie en streepjes zetten letter in woord
   if match:
    print(" ")
    print("Gefeliciteerd deze letter zit in het woord!")
    print(" ")
    
    for i in range(0, lengtewoord):
    
      if userinput == woord[i]:
        temp = temp[:i] + userinput +temp[i+1:]
    print(temp)
    print(" ")
#gebruikte letters worden weergeven    
    gebruikteletters.append(userinput)
    sorted(gebruikteletters)
    print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
#woord goed geraden felicitatie en opnieuw spelen optie
    if temp == woord:
      print(" ")
      print("Gefelicteerd je hebt het woord "+ str(woord)+ " goed geraden!")
      print(" ")
      again = input("Wil je nog een keer spelen? ja of nee? ")
    
      if again == "ja" or again == "Ja":
         print(" ")
         spel()
    
      else: 
         print("Tot ziens! :)")
         quit()

    print(" ")
#letter zit niet in woord
   else:
#letter is alfabetisch maar zit niet in woord dus beurten min 1  
    if x is True:
      print(" ")
      print("Jammer deze letter zit niet in het woord : (")
      counter = counter - 1
#galgje tekeningen voor elk aantal beurten
# nog 9 beurten
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#nog 8 beurten
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
#gebruikte letters worden weergeven    
             gebruikteletters.append(userinput)
             sorted(gebruikteletters)
             print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
             print(" ")
#nog 7 beurten
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
#gebruikte letters worden weergeven    
              gebruikteletters.append(userinput)
              sorted(gebruikteletters)
              print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
              print(" ")
#nog 6 beurten
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#nog 5 beurten
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#nog 4 beurten
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#nog 3 beurten
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#nog 2 beurten
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
#gebruikte letters worden weergeven    
       gebruikteletters.append(userinput)
       sorted(gebruikteletters)
       print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
       print(" ")
#nog 1 beurt
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
#gebruikte letters worden weergeven    
        gebruikteletters.append(userinput)
        sorted(gebruikteletters)
        print("Deze letters heb je al gebruikt "+ str(gebruikteletters)[1:-1] + " !")
        print(" ")
#beurten op --> dood
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
#geen beurten meer over dus woord wordt weergeven en er is een opnieuw spelen optie
       print("Jammer, je hebt verloren het woord was " + str(woord) + "!")
       print(" ")
       
       again = input("Wil je nog een keer spelen? ja of nee? ")
       
       if again == "ja" or again == "Ja":
         print(" ")
         spel()
       
       else: 
         print("Tot ziens! :)")
         quit()
#einde functie spel/gameloop
spel()