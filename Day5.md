### For Loop

> A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
> 
> 
> This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
> 
> With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
> 

```python
# Measure some strings:

words = ['cat', 'window', 'defenestrate']

for w in words:

    print(w, len(w))
```

```bash
# CONSOLE OUTPUT 
cat 3
window 6
defenestrate 12
```
```python
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
```

```bash
# CONSOLE OUTPUT
Apple
Peach
Pear
```

---

```python
# List of a student score 
student_scores = [
    85, 92, 78, 88, 95, 76, 84, 91, 72, 89,
    80, 93, 67, 75, 90, 82, 88, 79, 85, 94
]

total_score = sum(student_scores) # calculate sum of all item of the list with sum() 
print(f"Total score with sum() function {total_score}")

print(f"Max value with max() function: {max(student_scores)}") 
#max() will return the maximum value item inside the list 

sum = 0
for score in student_scores:
    sum += score

print(f"Total score with for loop method {sum}")

max_score = 0
for score in student_scores: 
    if score > max_score:
        max_score = score

print(f"Max value with for loop method {max_score}")
```
```bash
# CONSOLE OUTPUT 
Total score with sum() function 1683
Max value with max() function: 95
Total score with for loop method 1683
Max value with for loop method 95
```
---

### **The range() Function**

> To loop through a set of code a specified number of times, we can use the range() function,
> 
> 
> The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
> 

```python
#for number in range(a,b):
#   print (number)

# this will print the number in a range 1-9, the 10 is not included 
#for number in range(1,10):
#    print(number) 

# this will print the number in a range 1-11, the 11 is not included 
for number in range(1,11,3): # this will print by step 3 
    print(number) 
```

```bash
# OUTPUT CONSOLE
1
4
7
10
```

```python
## GAUSS CHALLENGE 
total = 0
for gauss in range(1,101):
    total += gauss

print(f"GAUSS VALUE : {total}")
```
---

### FizzBuzz Game

You are going to write a program that automatically prints the  solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.
- But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

```python
for number in range (1,101):
    if(number% 3 == 0 and number %5 == 0 ):
        print("FizzBuzz")
    elif(number % 3 == 0):
        print("Fizz")
    elif(number % 5 == 0):
        print("Buzz")
    else: 
        print(number)
```
---

### Password Generator Project

```python
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
```