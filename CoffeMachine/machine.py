# machine.py

# Global resources and profit
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# Menu with drink details (ingredients and costs)
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Function to handle resource deduction
def update_resources(drink_name):
    """Deduct the required ingredients from the resources."""
    for ingredient, amount in MENU[drink_name]["ingredients"].items():
        resources[ingredient] -= amount

# Function to check if there are enough resources to make the drink
def check_resources(drink_name):
    """Check if there are enough resources to make the drink."""
    for ingredient, amount in MENU[drink_name]["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

# Function to calculate the cost of a drink
def drink_cost(drink_name):
    """Return the cost of the drink."""
    return MENU[drink_name]["cost"]

# Function to process the transaction
def process_transaction(customer_money, drink_name):
    """Process the transaction and return True if the payment is sufficient."""
    cost = drink_cost(drink_name)
    if customer_money >= cost:
        global profit
        profit += cost
        change = round(customer_money - cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, you don't have enough money.")
        return False

# Function to calculate the total profit
def profit_money():
    """Return the total profit."""
    return profit

# Function to process the coins inserted by the user
def process_coins():
    """Return the total calculated from coins inserted by the user."""
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# Function to make the drink and update resources
def make_drink(drink_name):
    """Prepare the drink and update resources."""
    if check_resources(drink_name):  # Ensure resources are checked again before making the drink
        update_resources(drink_name)  # This will update the resources
        print(f"Here is your {drink_name} ☕")
