print("====================================")
print("         DHRUV'S QUESTIONARE       ")
print("====================================")

print()
print("1. Pokemon Quiz")
print("2. Minecraft Quiz")
print("3. Sports Quiz")

choice = input("Choose a game: ")

score = 0

# ======================
# POKEMON QUIZ
# ======================

if choice == "Pokemon Quiz":

    print()
    print("===== POKEMON QUIZ =====")
    print()

    answer = input("1. What type is Raichu? ")

    if answer.lower() == "electric":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong, The correct answer is electric")

    answer = input("2. What is Ash Ketchum's favourite pokemon? ")

    if answer.lower() == "pikachu":
        print("Correct!")
        score = score + 1
    else:
        print("Wrong, The correct answer is pikachu")

    answer = input("3. What type is Greninja? ")
    
    if answer.lower() == "water":
            print("Correct!")
            score = score + 1
    else:
         print("Wrong, The correct answer is water")

    answer = input("4. How many evolutions does Gyarados have? ")
     
    if answer.lower() == "2":
             print("Correct!")
             score = score + 1
    else:
        print("Wrong, The correct answer is 2")

    answer = input("5. How many mega evolutions does Lucario have? ")
             
    if answer.lower() == "2":
                     print("Correct!")
                     score = score + 1
    else:
        print("Wrong, The correct answer is 2")

    print()
    print("Your pokemon quiz score was:", score, "/ 5")

    # ==========================
    # MINECRAFT QUIZ
    # ==========================

elif choice == "Minecraft Quiz":

      print()
      print("===== MINECRAFT QUIZ =====")
      print()

      answer = input("1. Is there anything called the trinity in minecraft? ")
      
      if answer.lower() == "no":
              print("Correct!")
              score = score + 1
      else:
              print("Wrong, The correct answer is no")
      
      answer = input("2. How many mobs are in the end? ")
      
      if answer.lower() == "3":
              print("Correct!")
              score = score + 1
      else:
              print("Wrong, The correct answer is 3")
      
      answer = input("3. How many mobs are in the nether? ")
          
      if answer.lower() == "11":
                  print("Correct!")
                  score = score + 1
      else:
               print("Wrong, The correct answer is 11")
      
      answer = input("4. How many mobs are in the overworld? ")
           
      if answer.lower() == "67":
                   print("Correct!")
                   score = score + 1
      else:
              print("Wrong, The correct answer is 67")
      
      answer = input("5. What Minecraft mob can explode? ")
                   
      if answer.lower() == "creeper":
                    print("Correct!")
                    score = score + 1
      else:
              print("Wrong, The correct answer is creeper")
      
      print()
      print("Your minecraft quiz score was:", score, "/ 5")

    # ==========================
    # SPORTS QUIZ
    # ==========================

elif choice == "Sports Quiz":

      print()
      print("===== SPORTS QUIZ =====")
      print()

      answer = input("1. Which country held the first paralympics? ")
      
      if answer.lower() == "italy":
                  print("Correct!")
                  score = score + 1
      else:
              print("Wrong, The correct answer is italy")
      
      answer = input("2. Which country won the first paralympics? ")
      
      if answer.lower() == "italy":
              print("Correct!")
              score = score + 1
      else:
              print("Wrong, The correct answer is italy")
      
      answer = input("3. Who won the bbl last year? ")
          
      if answer.lower() == "perth scorchers":
                  print("Correct!")
                  score = score + 1
      else:
               print("Wrong, The correct answer is perth scorchers")
      
      answer = input("4. When is the next olympics? ")
           
      if answer.lower() == "2030":
                   print("Correct!")
                   score = score + 1
      else:
              print("Wrong, The correct answer is 2030")
      
      answer = input("5. Who won the first soccer world cup? ")
                   
      if answer.lower() == "brazil":
                           print("Correct!")
                           score = score + 1
      else:
              print("Wrong, The correct answer is brazil")
      
      print()
      print("Your pokemon quiz score was:", score, "/ 5")
      