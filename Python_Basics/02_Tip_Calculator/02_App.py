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



def tip_calculator():
    '''Generate Total Bill Amount Each Person will Pay Including Tip'''
    clear_screen()
    typing(" Welcome to the tip calculator! ")
    bill = float(input("What was the total bill? $"))
    tip = float(input("How much tip would you like to give? 10, 12, or 15? : "))
    spliting = int(input("How many people to split the bill? (at least 1) : "))
    each = (bill + (bill*(tip/100)))/spliting
    typing(f"Your Total Bill with Tip Would be : ${bill + (bill*(tip/100))}\nEach person should pay: ${round(each,2)}")

tip_calculator()