print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
spliting = int(input("How many people to split the bill? (at least 1) "))
each = (bill + (bill*(tip/100)))/spliting
print(f"Each person should pay: {round(each,2)}")
