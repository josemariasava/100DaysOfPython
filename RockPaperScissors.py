import random
# string for rock, paper, scissors 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_list = [rock,paper,scissors]

print("What do you choose? 0 for rock, 1 for paper, 2 for scissors")

user_input = int(input())

print(game_list[user_input])


computer_input = random.randint(0,2)
print(f"Computer chose: {computer_input}")

print(game_list[computer_input])

# combination for win-lose 
if(user_input >= 3 or user_input < 0): 
    print("Invalid number! You lose!")
elif (user_input == 0 and computer_input == 2):
    print("You win!")
elif(computer_input == 0 and user_input == 2):
    print("You lose!")
elif(computer_input > user_input):
    print("You lose!")
elif(user_input > computer_input):
    print("You win!")
elif(computer_input == user_input):
    print("This is a draw!")

