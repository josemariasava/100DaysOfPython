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
