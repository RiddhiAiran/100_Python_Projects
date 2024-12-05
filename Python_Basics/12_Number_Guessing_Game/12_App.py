from logo import logo
import random


def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Generated Random Number
    random_num = random.randint(1,100)
    # Set Difficulty
    attempts = 0
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        attempts = 10
    elif level == 'hard':
        attempts = 5
    else:
        print("Invalid input! Defaulting to 'hard' mode.")
        attempts = 5

    while attempts > 0:
        guess = input("Make a Guess: ")
        if not guess.isdigit():
            print("Please enter a valid number!")
            continue
        guess = int(guess)
        if guess == random_num:
            print("You got it! 🎉")
            return
        elif guess > random_num:
            print("Too High!")
        else:
            print("Too Low!")

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You've run out of attempts. You lose! 😢")
            print(f"The correct number was {random_num}.")

# Call the function to start the game
number_guessing_game()

