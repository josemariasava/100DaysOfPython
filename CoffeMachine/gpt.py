from machine import resources, MENU, dict_of_resources, process_coins, transaction, drink_cost, profit_money, make_drink

def check_resources(drink_name):
    """Check if there are enough resources for the chosen drink."""
    for ingredient in dict_of_resources:
        required_amount = dict_of_resources[ingredient](MENU, drink_name)
        if resources[ingredient] < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True

def print_report():
    """Print the current resources and profit."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit_money()}")

def process_order(choice):
    """Process the order by checking resources, handling payment, and making the drink."""
    if not check_resources(choice):
        return

    # Process payment
    user_payment = process_coins()
    if transaction(user_payment, drink_cost(MENU, choice)):
        make_drink(choice)  # Updates the resources in make_drink

def main():
    """Main loop for taking orders and managing the coffee machine."""
    active = True
    while active:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            active = False
        elif choice == "report":
            print_report()
        elif choice in MENU:
            process_order(choice)
        else:
            print("Invalid choice. Please select a valid drink.")

if __name__ == "__main__":
    main()
