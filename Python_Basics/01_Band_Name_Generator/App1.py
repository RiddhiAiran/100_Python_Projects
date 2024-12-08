import os
import time

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def typing(message):
    for letter in message:
        print(letter, end ='', flush=True)
        time.sleep(0.01)
    print()

def band_name_generator():
    """Generate band name using user inputs"""
    clear_screen()
    typing("Welcome to the Basic Band Name Generator.")
    city = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")
    typing(f"Your Band Name Could be : {city} {pet}")

band_name_generator()