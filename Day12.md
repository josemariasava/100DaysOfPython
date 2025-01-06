### Local scope

> A variable created inside a function belongs to the *local scope* of that function, and can only be used inside that function.
> 

```python
# A variable created inside a function is available inside that function:
def myfunc():
  x = 300
  print(x)

myfunc() 
```
---
### **Function Inside Function**

> The local variable can be accessed from a function within the function:
> 

```python
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() 
```
---
### Global Scope

> A variable created in the main body of the Python code is a global variable and belongs to the global scope.Global variables are available from within any scope, global and local.
> 

```python
x = 300

def myfunc():
  print(x)

myfunc()

print(x) 
```
---
### Global Keyword

> If you need to create a global variable, but are stuck in the local scope, you can use the `global` keyword.The `global` keyword makes the variable global.
> 

```python
#If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = 300
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

def myfunc1():

myfunc()

print(x) 
```
---
### Nonlocal Keyword

The `nonlocal` keyword is used to work with variables inside nested functions.

The `nonlocal` keyword makes the variable belong to the outer function.

```python
# If you use the nonlocal keyword, the variable will belong to the outer function:
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1()) 
```
---
### **Python Constants**

> A Python Constant is a variable whose value cannot be changed throughout the program.
> 

```python

# create a separate constant.py file
PI = 3.14
GRAVITY = 9.8
```

```python

# main.py file
import constant as const

print('Value of PI:', cons.PI)
print('Value of Gravitational force:', cons.GRAVITY)
```
---

### Guess the number

**function.py**

```python
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
```

**main.py**

```python
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
```