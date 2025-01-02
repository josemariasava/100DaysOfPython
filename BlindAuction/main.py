import function

# print the logo 
print(function.logo)

#Define empty dictionary and bool value to run/stop the code execution 

bids = {} # empty dict 
run = False # bool var 

# while loop 
while not run:
    # call add_bidd from function.py 
    function.add_bid(bids)

    # Ask if continue with another bid 
    bid_continue = input("Are there any other bidders? Type 'yes or no' \n").lower()

    if bid_continue == 'no':
        run = True
        function.find_best_bid(bids)
    elif bid_continue == "yes":
        function.clear()