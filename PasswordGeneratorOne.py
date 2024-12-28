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

# Declaration of password as a list 
password_list = []

# iterate letterls list 
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

# iterate symbols list 
for symbol in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

# iterate numbers list 
for number in range(0,nr_numbers):
    password_list.append(random.choice(numbers))


random.shuffle(password_list) # randomize item in my list 

print(password_list) # print in list format 

