import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if  0<= user_choice <= 2:
    print(symbols[user_choice])
computer = random.randint(0,2)
print(f"Computer choose : {symbols[computer]}")

if  0 > user_choice > 2:
    print("Please Enter Valid Input")
elif computer == user_choice:
    print("Match Tie")
elif (user_choice == 0 and computer == 2) or (user_choice == 2 and compile == 1) or (user_choice == 1 and computer == 0):
    print("You win!")
else:
    print("Computer Win!")
