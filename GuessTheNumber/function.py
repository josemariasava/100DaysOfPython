
logo = """
   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|                                                                                  
"""

def set_difficulty():
    """Set the difficulty for the user -> easy = 10 attempts | hard = 5 attempts"""
    difficult = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficult == 'easy':
        attempts = 10
        return attempts
    else: 
        attempts = 5
        return attempts
    
def check_answer(user,num,turns):
    if user > num:
        print("Too high.")
        return turns - 1
    elif user < num:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The number was {num}")


def guess_number():
    """Ask the user input"""
    guess= int(input("Make a guess: "))
    return guess