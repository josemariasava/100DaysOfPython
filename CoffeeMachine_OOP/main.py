from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from time import sleep



def welcome_message():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----' 
    
          ------ MENU ------ 
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------
    
          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')

# Create objects 
menu = Menu() # Construct an object of Menu class 
money_machine = MoneyMachine() # Construct an object of MoneyMachine class 
coffe_maker = CoffeeMaker() # Construct an object of CoffeMaker class 

# Bool to loop and run the machine 
machine_on = True 

while machine_on: 
    welcome_message() 
    options = menu.get_items() 

    user_choice = str(input(f"What would you like? \n {options}: ")).strip().lower()
    if user_choice == 'off':
        print('\033[31m<<THE END>>\033[m')
        machine_on = False
    elif user_choice == 'report':
        coffe_maker.report()
        money_machine.report()
    elif user_choice == 'main':
        coffe_maker.refill()
    else: 
        drink = menu.find_drink(user_choice)
        resources = coffe_maker.is_resource_sufficient(drink)
        money_ok = money_machine.make_payment(drink.cost)
        if resources and money_ok:
            print("Thank you! Here comes your drink...")
            coffe_maker.make_coffee(drink)
            sleep(5)