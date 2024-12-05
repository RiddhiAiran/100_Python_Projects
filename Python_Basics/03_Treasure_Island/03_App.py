print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     "=.|                  |
|___________________|__"=._o"-._        "=.______________|___________________
          |                "=._o"=._      _"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; "=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  ` ,  "-._"-._   ". '__|___________________
          |           |o"=._ , " ; .". ,  "-._"-._; ;              |
 _________|___________| ;-.o"=._; ."  '."\ . "-._ /_______________|_______
|                   | |o;    "-.o"=._`  ' " ,__.--o;   |
|___________________|_| ;     (#) -.o "=._.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      ".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************  ''')
print("Welcome to Treasure Island\n Your Mission is to find the Treasure.\n You're at the cross road. Where do you want to go?")
Road = input("Type 'left' or 'Right'\n").lower()

if Road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type 'wait' to wait for a baot. Type 'swim' to swim across.\n").lower()
    if lake == 'wait':
        print("You have arrived at the island unharmed. There is a house with 3 doors.")
        door = input("One Red, One Yellow and One Blue. Which colour do you choose?\n").lower()
        if door == "yellow":
            print("Congrats! you found the treasure..!!")
        elif door == "red":
            print("Burned by fire!")
        elif door == "blue":
            print("Eaten by Beasts! Game Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout, Game Over!")
else:
    print("Fall into a hole, Game Over!")