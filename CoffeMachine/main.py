from machine import resources
from machine import MENU
from machine import dict_of_resources
from machine import process_coins
from machine import transaction
from machine import drink_cost 
from machine import profit_money

active = True

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]



while active:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        active = False # exit the execution if maintenance type off
    elif choice == "report":
        print(f"water: {water}")
        print(f"milk: {milk}")
        print(f"coffee: {coffee}")
        print(f"money: {profit_money()}")
    else:
        #Check the availability of the resources 
        if water < dict_of_resources["water"](MENU,choice):
            print("Sorry not enough water")
            active = False
        elif milk < dict_of_resources["milk"](MENU,choice):
            print("Sorry not enough milk")
            active = False 
        elif coffee < dict_of_resources["coffee"](MENU,choice):
            print("Sorry not enough coffee")
            active = False
        else:
            user_payment = process_coins()
            transaction(user_payment,drink_cost(MENU,choice))
