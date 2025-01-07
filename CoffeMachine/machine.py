MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def water_needed(MENU,drink):
    """Return the amount of water needed to make the drink in args"""
    waterin = MENU[drink]["ingredients"]["water"]
    return waterin

def milk_needed(MENU,drink):
    """Return the amount of milk needed to make the drink in args"""
    milkin = 0
    #check if the drink is an espresso - no milk needed 
    if drink != "espresso":
        milkin = MENU[drink]["ingredients"]["milk"]
        return milkin
    else: 
        milkin = 0
        return milkin

def coffee_needed(MENU,drink):
    """Return the amount of coffee needed to male the drik in args"""
    coffein = MENU[drink]["ingredients"]["coffee"]
    return coffein

def drink_cost(MENU,drink):
    """Return the cost of the drink in args"""
    cost = MENU[drink]["cost"]
    return cost

def transaction(customer_money,cost_drink):
    """Return true if payment is accepted """
    if customer_money >= cost_drink:
        change = round(customer_money - cost_drink,2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost_drink
        return True 
    else: 
        print("Sorry you don't have enough money.")
        return False 

def profit_money():
    return profit

def process_coins():
    """"Return the toal calculated from coins inserter by the user"""
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickeles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


dict_of_resources ={ 
    "water": water_needed, 
    "milk": milk_needed,
    "coffee": coffee_needed
}