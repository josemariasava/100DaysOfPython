from machine import resources, MENU, process_coins, process_transaction, drink_cost, profit_money, make_drink, check_resources

def print_report():
    """Print the current resources and profit."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit_money()}")

def process_order(choice):
    """Process the order by checking resources, handling payment, and making the drink."""
    if check_resources(choice):  # Check if there are enough resources
        user_payment = process_coins()
        if process_transaction(user_payment, choice):
            make_drink(choice)  # This will update the resources
    else:
        print(f"Sorry, not enough resources to make {choice}.")

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
