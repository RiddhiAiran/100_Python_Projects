from logo import first
import random 

print(first)

cards = [1,2,3,4,5,6,7,8,9,10,10,10]

user_cards = [random.choice(cards),random.choice(cards)]
dealer_cards = [random.choice(cards), random.choice(cards)]

print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"Computer's first card: {dealer_cards[0]}")
choose = input("Type 'y' to get another card, type 'n' to pass: ")

