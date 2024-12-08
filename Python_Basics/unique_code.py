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
        time.sleep(0.1)
    print()

