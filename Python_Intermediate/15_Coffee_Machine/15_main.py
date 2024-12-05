from data import MENU, resources

def is_sufficient_ingredients(ingredients,resources):
    '''Returns True when the ingredients are sufficient to make the drink'''
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f'Sorry There is not Enough {item}')
            return False
    return True

def insert_cash(q, d, n, p):
    '''Calculate Total Cash with the Inserted Coins'''
    total = (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01)
    return total

def deduct_ingredients(ingredients, resources):
    '''Deduct the ingredients from the resources to make the coffee.'''
    for items in ingredients:
        resources[items] -= ingredients[items]

money = 0
while True:
    print("Welcome To the Coffee Machine!")
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        break
    elif choice == 'report':
        # Display current resources and money
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if choice in MENU:
            drink = MENU[choice]
            ingredients = drink["ingredients"]
            cost = drink["cost"]

            if is_sufficient_ingredients(ingredients, resources):
                print(f"The cost of your {choice} is ${cost}.")
                # Get the Coins
                print("Please insert coins.")
                q = int(input("Quarters: "))
                d = int(input("Dimes: "))
                n = int(input("Nickels: "))
                p = int(input("Pennies: "))
                total_inserted = insert_cash(q, d, n, p)
                if total_inserted < cost:
                    print("Sorry, that's not enough money. Money refunded.")
                else:
                    change = round(total_inserted - cost, 2)
                    print(f"Here is ${change} in change.")
                    print(f"Enjoy your {choice}!")

                    deduct_ingredients(ingredients, resources)
                    money += cost
            else:
                print("Unable to process your request due to insufficient resources.")
        else:
            print("Invalid choice. Please select a valid option.")