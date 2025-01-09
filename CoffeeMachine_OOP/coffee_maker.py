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