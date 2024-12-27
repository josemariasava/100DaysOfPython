#Welcome 
# How many letters 
# How many symbols 
# How many numbers 
import random

# letters list 
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  # lowercase letters
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'   # uppercase letters
]

# simbol list 
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

# number list 
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]

print("--- Password generator --- \n")

nr_letters = int(input("How many letters? \n"))
nr_symbols = int(input("How many symbols? \n"))
nr_numbers = int(input("How many numbers? \n"))

#Easy Level 
password = "" # empty string 

# Loop the letters 
for char in range(1,nr_letters+1):
    random_char= random.choice(letters)
    password += random_char

# Loop the symbols 
for symbol in range(1, nr_symbols +1):
    random_symbol = random.choice(symbols)
    password += random_symbol

# Loop the numbers 
for number in range(1,nr_numbers +1):
    random_number = random.choice(numbers)
    password += random_number

print(f"Yuor easy level password is: {password} \n")

# try to randomize the password generated 
# Hard Level 

random_password = list(password) #Cast string to list to use shuffle() function of random module 

random.shuffle(random_password)

print("Your hard level password is: ")
print(''.join(random_password))

