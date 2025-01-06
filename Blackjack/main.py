from utils import deal_card
from utils import calculate_score
from utils import compare
from utils import clear

def play_game():
    # empty lists for user and computer 
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False # bool to check if game finish 

    # loop to assign 2 cards for each user. 
    # _ sign because we need to run just the loop 
    for _ in range(2):
        user_cards.append(deal_card()) # .append() add an element to list
        computer_cards.append(deal_card()) 

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {user_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21: 
            game_over = True
        else:
            user_deal=input("Type 'y' to get another card, type 'n' to pass:  ").lower()
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_cards = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear() 
    play_game()
