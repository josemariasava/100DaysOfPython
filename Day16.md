### Create a Class

> To create a class, use the keyword `class`:
> 

```python
class MyClass:
  x = 5
```

### Create Object

> Now we can use the class named MyClass to create objects:
> 

```python
p1 = MyClass()
print(p1.x) 
```

### The __init__() Function

> The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in `__init__()` function.
All classes have a function called `__init__()`, which is always executed when the class is being initiated.
Use the `__init__()` function to assign values to object properties, or other  operations that are necessary to do when the object is being created:
> 

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
```
---

### Turtle example

```python
import turtle # import module 

timmy = turtle.Turtle() # creating an object [timmy] of class Turtle() 
print(timmy) # turtle.Turtle object at 0x70f15d7fe210> Console output of print of an object, is the memory address where is stored

# call methods from the class Turtle()
timmy.shape("turtle") 
timmy.color("coral") 
timmy.forward(100)

my_screen = turtle.Screen() # creating an object [my_screen] of class Screen()
print(my_screen.canvheight)

my_screen.exitonclick() 
```

---

### Packages

> Code from other developer. Is it possible to browse all the python packages in Python Package Index: https://pypi.org/
> 

**Prettytable package example**

```python
rom prettytable import PrettyTable  #import prettytable package 

table = PrettyTable() # construct a PrettyTable() Object 

table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align = "l"

print(table)
```

---

### OOP coffe machine

[How do I print colored text to the terminal?](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)

**Coffe_maker** 

```python
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f'''\033[32m
             )))
            (((
          +-----+
          |     |] - Here's your {order.name}. Enjoy! :)
          `-----'
        \33[m''')
    
    def refill(self):
        """Refill machine with resources - access with 'main' word in choice selection"""
        self.resources['water'] += int(input("How many ml of water ? : "))
        self.resources['milk'] += int(input("How many ml of milk ? : ) "))
        self.resources['coffee'] += int(input("How many g of coffe ? : "))
```

**money_machine**

```python
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
    
    
```

**menu**

```python
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
```

**main** 

```python
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
```