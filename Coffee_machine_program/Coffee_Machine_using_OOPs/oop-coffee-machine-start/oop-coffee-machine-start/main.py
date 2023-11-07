from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    item = menu.get_items()
    choice = input(f"Enter you preference {item}: ").lower()
    if choice == "off":
        is_on = False
    
    elif choice == "report":
        #Make the report
        coffee_maker.report()
        money_machine.report()
    #check whether the ingredients are sufficient
    else:
        drink = menu.find_drink(choice)
        #Checking whether the resources is suffiecient.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

            
        



