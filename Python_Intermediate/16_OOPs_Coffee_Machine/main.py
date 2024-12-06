# import libraries
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    choice = input(f"What would you like? ({menu.get_items()}) : ")
    if choice == 'off':
        break
    elif choice == 'report':
        machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice) # drink is the menu_item object
        if machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            machine.make_coffee(drink)






