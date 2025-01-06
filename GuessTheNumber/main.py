from random import randint
import function

def game():
    print(function.logo)
    print("Welcome to Guess the Number! ")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number with range 1-100 
    number = randint(1, 100) 
    # just to debug the code 
    print(f'The number to guess is: {number}')

    # chose difficult
    level = function.set_difficulty()
    

    guess = 0

    while guess != number:
        print(f'You have {level} attempts remaining to guess the number')
        # Guess the number
        guess = function.guess_number()
        # Check the result and update the user attempts
        level = function.check_answer(guess,number,level)
        if level == 0:
            print("You've run out of guesses, you lose.")
            return # exit and END the function - game 
        elif guess != number: 
            print("Guess again.")

game()
