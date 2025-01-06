# import modules 
from game_data import data
import random 
import function

score = 0
run = True
 # display art
print(function.main_logo)
account_b = random.choice(data)

while run: 

    # Pick random data from game_data list 
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    # Format correctly the data of each record of game_data 
    print(f'Compare A: {function.format_data(account_a)}')

    print(function.vs_logo)

    print(f'Compare B: {function.format_data(account_b)}')

    # Ask user for a guess --> A or B 
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    function.clear()

    # Check if user input is correct 
        # Get the followr count of each account 
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = function.check_data(guess, a_follower,b_follower)
        # if right the game continue 
    if is_correct:
        score += 1
        print(f'You are right! Your current score is: {score}')
    else:
        print(f'Wrong answer. Your final score is: {score}')
        run = False


