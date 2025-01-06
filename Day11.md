### Functions to be used

[Python Lists  |  Python Education  |  Google for Developers](https://developers.google.com/edu/python/lists#list-methods)

[Built-in Functions](https://docs.python.org/3/library/functions.html#sum)

### Simple Blackjack game

**Utils.py**

```python
import random

def deal_card():
    """returns a random card from the deck"""
    #List of cards 
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """return the total score of the cards list"""
    if sum(cards) == 21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    """Compare the scores and return the winner of the game"""
    if user_score == computer_score:
        return "Its a Draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "Opponent went over 21. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def clear():
    """Clear the console by printing 20 times a new line char"""
    print("\n"*20)

```

**Main.py**

```python
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

```