import random # We wil use random in calculating coin toss and chance algorithm

def integer_division(HP): #This is function I will use to print how much HP Heros have in |
    return int(HP)/int(2) * "|"

def First_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP): #This is the one displays First Hero's HP on the left
    print First_Hero, "                                                              " + Second_Hero
    print "HP" + "[" + str(First_Hero_HP) + "]" + ":" + " " + str(integer_division(First_Hero_HP)), "     " + "HP" + "[" + str(Second_Hero_HP) + "]" + ":" + " " + str(integer_division(Second_Hero_HP))

def Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP): #This is the one displays Second Hero's HP on the left
    print Second_Hero, "                                                             " + First_Hero
    print "HP" + "[" + str(Second_Hero_HP) + "]" + ":" + " " + str(integer_division(int(Second_Hero_HP))), "     " + "HP" + "[" + str(First_Hero_HP) + "]" + ":" + " " + str(integer_division(int(First_Hero_HP)))

def Strike(Hero): #This function prints which hero attacks and makes sure user gives valid magnitude between 1 and 50
    print "---------------" + " " + Hero + " " + "Attacks !! ---------------"
    while True:
        Magnitude = raw_input("Choose your attack magnitude between 1 and 50: ")
        if 1 <= int(Magnitude) <= 50:
            return Magnitude
        elif int(Magnitude) > 50:
            print "The attack magnitude must be between 1 and 50."
            continue
        elif int(Magnitude) < 1:
            print "The attack magnitude must be between 1 and 50."
            continue
        else:
            print "The attack magnitude must be between 1 and 50."
            continue

def Hit_Chance_algorith(Magnitude, Attacking_Hero, Defending_Hero_HP): #My algorithm which calculates chance of hitting enemy hero(Chance decreases as magnitude increases)
    Hit_Chance = random.randint(1, 100)
    if Hit_Chance <= (100-int(Magnitude)):
        print Attacking_Hero + " " + "hit" + " " + str(Magnitude) + " " + "damage!!"
        return Attacking_Hero + " " + "hit" + " " + str(Magnitude) + " " + "damage!!"
    elif Hit_Chance > (100-int(Magnitude)):
        print "Ooopsy!" + " " + Attacking_Hero + " " + "missed the attack!"
        return "Ooopsy!" + " " + Attacking_Hero + " " + "missed the attack!"

def First_Player_Choose_Name(): #Function that define first players name
    while True:
        print "----- First Hero -----"
        First_Hero = raw_input("Please type your hero's name: ")
        if First_Hero == " ": #Blank hero name error
            print "Hero's name cannot be blank. Please enter valid name again."
            continue
        elif First_Hero == "": #Blank hero name error
            print "Hero's name cannot be blank. Please enter valid name again."
            continue
        elif type(First_Hero) != type("I'm a string"):  # Hero name should nothing other than string
            print "Hero's name should be string"
            continue
        elif type(First_Hero) == type("I'm a string"): #Hero name should be string
            print "First hero's name is" + " " + First_Hero
            break
        else:
            print "Enter valid name again."
            continue
    return First_Hero

def Second_Player_Choose_Name(): #Function that define second players name
    while True:
        print "----- Second Hero -----"
        Second_Hero = raw_input("Please type your hero's name: ")
        if Second_Hero == " ": #Blank hero name error
            print "Hero's name cannot be blank. Please enter valid name again."
            continue
        elif Second_Hero == "": #Blank hero name error
            print "Hero's name cannot be blank. Please enter valid name again."
            continue
        elif type(Second_Hero) != type("I'm a string"):  # Hero name should nothing other than string
            print "Hero's name should be string"
            continue
        elif Second_Hero == First_Hero: #If second player enters same name as first one
            print First_Hero + " " + "is taken, please choose another name!"
            continue
        elif type(Second_Hero) == type("I'm a string"): #Hero name should be string
            print "Second hero's name is" + " " + Second_Hero
            break
        else:
            print "Enter valid name again."
            continue
    return Second_Hero

def Coin_Toss(): #This function determines which Hero starts first by tossing a coin
    CoinTossList = ["Coin toss result:" + " " + First_Hero + " " + "starts first!", "Coin toss result:" + " " + Second_Hero + " " + "starts first!"]
    CoinToss = random.choice(CoinTossList)  # Decides which hero starts first
    return CoinToss

def Strike_Turn_by_Turn(Magnitude, Second_input, First_Hero_HP, Second_Hero_HP, Second_Heros_Turn_HP_Status): #A loop that continues allows FirstHero and Second Hero to strike each other untill either one's health drops below zero
    Turn_Decider = Second_input #Turn decider decides on which hero will start based on output of Hit_Chance_algorith
    while Second_Hero_HP > int(0) and First_Hero_HP > int(0):
        if Turn_Decider == Second_Hero + " " + "hit" + " " + str(Magnitude) + " " + "damage!!":
            Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
            Magnitude = Strike(First_Hero)
            First_Hero_HP = int(First_Hero_HP) - int(Magnitude)
            Turn_Decider = Hit_Chance_algorith(Magnitude, First_Hero, Second_Hero_HP)
            continue
        elif Turn_Decider == First_Hero + " " + "hit" + " " + str(Magnitude) + " " + "damage!!":
            Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
            Magnitude = Strike(Second_Hero)
            Second_Hero_HP = int(Second_Hero_HP) - int(Magnitude)
            Turn_Decider = Hit_Chance_algorith(Magnitude, Second_Hero, First_Hero_HP)
            continue
        elif Turn_Decider == "Ooopsy!" + " " + Second_Hero + " " + "missed the attack!":
            Magnitude = Strike(First_Hero)
            Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
            Turn_Decider = Hit_Chance_algorith(Magnitude, First_Hero, Second_Hero_HP)
            continue
        elif Turn_Decider == "Ooopsy!" + " " + First_Hero + " " + "missed the attack!":
            Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
            Magnitude = Strike(Second_Hero)
            Turn_Decider = Hit_Chance_algorith(Magnitude, Second_Hero, First_Hero_HP)
            continue
    Who_Won(First_Hero_HP, Second_Hero_HP)

def Fight_Starts(): #This function starts fighting based on result of coin toss
    if CoinToss == "Coin toss result:" + " " + First_Hero + " " + "starts first!":
        First_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
        Magnitude = Strike(First_Hero)
        Turn_Decider = Hit_Chance_algorith(Magnitude, First_Hero, Second_Hero_HP)
        Strike_Turn_by_Turn(Magnitude, Turn_Decider, First_Hero_HP, Second_Hero_HP, First_Heros_Turn_HP_Status)
        Who_Won(First_Hero_HP, Second_Hero_HP)

    elif CoinToss == "Coin toss result:" + " " + Second_Hero + " " + "starts first!":
        Second_Heros_Turn_HP_Status(First_Hero_HP, Second_Hero_HP)
        Magnitude = Strike(Second_Hero)
        Turn_Decider = Hit_Chance_algorith(Magnitude, Second_Hero, First_Hero_HP)
        Strike_Turn_by_Turn(Magnitude, Turn_Decider, First_Hero_HP, Second_Hero_HP, Second_Heros_Turn_HP_Status)
        Who_Won(First_Hero_HP, Second_Hero_HP)

def Who_Won(First_Hero_HP, Second_Hero_HP):   #Function that determines who won and prints its name as below
    if First_Hero_HP < int(0): # If First hero health drops below 0
        print "###################################################################"
        print "###########################" + " " + Second_Hero + " Wins !!" + "##############################"
        print "###################################################################"
    elif Second_Hero_HP < int(0): # If Second hero health drops below 0
        print "###################################################################"
        print "###########################" + " " + First_Hero + " Wins !!" + "##############################"
        print "###################################################################"

def Play_Another_Round(First_Hero_HP, Second_Hero_HP): #This function asks player if he wants to play again, if not finishes game
    while True:
        answer = raw_input("Do you want to play another round (Yes or No)? : ")
        if answer == "Yes":
            CoinToss = Coin_Toss()
            print CoinToss
            First_Hero_HP = int(100)
            Second_Hero_HP = int(100)
            Fight_Starts()
            Play_Another_Round(First_Hero_HP, Second_Hero_HP)
        elif answer == "No":
            print "Thanks for playing! See you again!"
            break
        else:
            print "Enter valid input (Yes or No)"
            continue

First_Hero = First_Player_Choose_Name() # This is where user input assigned to First_Hero
Second_Hero = Second_Player_Choose_Name() # This is where user input assigned to Second_Hero

CoinToss = Coin_Toss()
print CoinToss

First_Hero_HP = int(100) # First Hero initial HP
Second_Hero_HP = int(100) # Second Hero Initial HP

Fight_Starts()
Play_Another_Round(First_Hero_HP, Second_Hero_HP)

