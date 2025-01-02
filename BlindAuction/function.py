# Definde logo 
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Add bid 
def add_bid(dict):

    #Ask the user for key and value 

    name = input("What is your name?: ") # key 
    price = int(input("What is your bid?: $ ")) # value 

    dict[name] = price

    return dict

# find best bid 
def find_best_bid(dict):
    highest = 0 
    winner = ""
    for bid in dict:
        bid_price = dict[bid]
        if bid_price > highest: 
            highest = bid_price
            winner = bid
    print(f'The winners is {winner} with a bid of ${highest}')


# Clear the console by printing 15 new line
def clear():
    print("\n" * 15)