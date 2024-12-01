print("Welcome to Python Pizza Deliveries!")
size = input("What size Pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N : ").lower()
extra_cheese = input("Do you want extra cheese? Y or N : ").lower()
Bill = 0

if size == "S":
    Bill += 15
elif size == "M":
    Bill += 20
elif size == "L":
    Bill += 25
else:
    print("Enter Valid Value")

if pepperoni == 'y':
    if size == "S":
        Bill += 2
    else:
        Bill += 3

if extra_cheese == 'y':
    Bill += 1

print(f"Your Total Bill Will be : ${Bill}.")