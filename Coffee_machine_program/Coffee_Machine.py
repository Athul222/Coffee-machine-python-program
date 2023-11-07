#Creating a coffee machine..
from Coffee_data import MENU , resources

profit = 0


def is_resource_suffiecient(order_ingredients):
    """Returns True when order can be made else false if the ingredients are insufficient."""
    for item in order_ingredients:
        #is_there_ingredient = true
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is no enough {item} left.")
            return False #It can be considered as is_there_ingredient = false
    return True # Else is_there_ingredient = True


def is_transaction_successfull(money_received , drink_cost):
    if money_received >= drink_cost:
        #Making change variable to save the change when the user gives more money.
        change = round(money_received - drink_cost , 2)
        print(f"Here is ${change} in change")
        global profit #Making profit global for eassy access inside this function.
        profit += drink_cost #Adding the cost of drink to the profit and storing it.
        return True
    else:
        print("Sorry, that's not enough money, money refunded. ")
        return False


def make_coffee(drink_name , order_of_incredient):
    """Deduct the received ingredients from the resources. """
    for item in order_of_incredient:
        resources[item] -= order_of_incredient[item]
    print(f"Here is your {choice}. Enjoy it!")

def process_coins(): #Don't take any parameter.
    """Return total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quaters: ")) * 0.25
    total += int(input("How many Dimes: ")) * 0.1
    total += int(input("How many Nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total

        
is_on = True
while is_on:
    #Asking the user what whould they like to have
    choice = input("What would like to order(espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}") 
        
    else:
        #Then the user will defenitely select one of any drinks
        drink = MENU[choice]
        
        #Calling the 
        if is_resource_suffiecient(drink["ingredients"]):
            #If all the required resource is available then we proceed with making it.
            
            payment = process_coins() #Used to check whether the payment is done or not.
            if is_transaction_successfull(payment , drink["cost"]):
                make_coffee(choice , drink["ingredients"])
                