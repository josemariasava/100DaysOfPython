### Build Hangman game

- hangman_art
    
    ```python
    hangman_stages = [
        '''
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
         O   |
        /|\  |
             |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
         O   |
        /|   |
             |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
         O   |
             |
             |
             |
             |
        -----|-----
        ''', 
        '''
         -----
         |   |
             |
             |
             |
             |
             |
        -----|-----
        '''
    ]
    
    hangman_logo ='''
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       
    '''
    
    ```
    

```python
# import modules 
import random # import everything from this module 
from Hangman_words import word_list # Import just the single list from the file 
from Hangman_art import hangman_stages,hangman_logo # Import just the single list from the file 

word_to_guess = random.choice(word_list).lower() # random assign to word one of the list 
word_length = len(word_to_guess) # length of the string 
placeholder = "" # empty string for our placeholder

game_over = False # boolean value to running the game 
correct_letters = []
lives = 6 # lives of the user

print(hangman_logo)

for place in range(word_length): # loop the word to display the placeholder 
    placeholder+="-"

print(word_to_guess)
print(placeholder) 

while not game_over: 
    print(f"-*-*-*-*-*-*-*{lives}/6 LIVES LEFT-*-*-*-*-*-*-*")

    guess_letter = input("Guess a letter: ").lower() 
    display_word = "" # empty string for user 

    if guess_letter in correct_letters:
        print(f"You've already guessed the letter: {guess_letter} ")

    for letter in word_to_guess:
        if letter == guess_letter: 
            display_word+= letter
            correct_letters.append(guess_letter)

        elif letter in correct_letters:
            display_word+= letter

        else:
            display_word+="-"

    if guess_letter not in word_to_guess:
        lives -= 1
        print(f"You guessed {guess_letter} but is not in the word. You lose a life. ")
        
        if lives == 0:
            game_over = True
            print("-*-*-*-*-*-*-*YOU LOSE-*-*-*-*-*-*-*")

    print(display_word)

    if "-" not in display_word:
        game_over = True
        print("-*-*-*-*-*-*-*YOU WIN-*-*-*-*-*-*-*")
    
    print(hangman_stages[lives])
```