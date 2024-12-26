### Random Module

> A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable
> 

### Integer numbers

```python
### https://docs.python.org/3/library/random.html ### 
#Functions for integers
#random.randrange(stop)
#random.randrange(start, stop[, step])
#   Return a randomly selected element from range(start, stop, step).

import random #random module 

a = random.randint(1,100); #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

print(f'The random integrer generated is {a}')

#OUTPUT CONSOLE 
# The random integrer generated is n where n is in the range 1,100 
```
### Floating point numbers

```python
import random #random module 

b = random.random() # Return the next random floating-point number in the range 0.0 <= X < 1.0

print(f'The random floating point using random() is {b}')

# Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
c = random. uniform(0,100)

print(f'The random floating point using uniform() is {c}')
```
### Head-Tails using randomisation

```python
# Create a coin flip program using randomisation in Python. It should print "Heads or "Tails"

import random

# Generate random number with a range 0-1 
number = random.randint(0,1) # this will generate or 0 or 1 

if(number == 0):
    print("Heads")
else:
    print("Tails")
```
---

### Creating a module

- create a file named my_module.py
- add var and functions to it
- you can recall a module simply by using **import**

```python
# This is the content of the file my_module.py 
my_number = 3.14
```

```python
# This is the content of the file main.py 
import my_module

print(my_module.my_number)

#OUTPUT CONSOLE 
# 3.14
```
---
### Lists

> In Python, a list is a built-in dynamic sized array (automatically grows and shrinks) that is used to store an ordered collection of items. We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.
- List can contain duplicate items.
- List in Python are Mutable. Hence, we can modify, replace or delete the items.
- List are ordered. It maintain the order of elements based on how they are added.
- Accessing items in List can be done directly using their position (index), starting from 0.
>
```python
# LIST EXAMPLES 

list_example = [item1,item2]

list_one = ["item0", "item1", "item2"] # declaration of a list 
#index        #0        #1       #2

print(list_one[0]) # printing the first item of the list 

# element starts from position 0 to position n 

print(list_one[-1]) # printing the last item of the list 

# you can access the list in opposite way by using the negative index 

list_one[1] = "index_item1" #replacing item in a list 

print(list_one[1]) # this will print the new item replaced before 

list_one.append("index_item3") # append() will add to the end of the list one new item 

print(list_one) # in this way we can print all the item inside a list 
```

For all the functions related to list referee to: https://docs.python.org/3/tutorial/datastructures.html

---

### Error Handling

```python
# Declaration of list states_of_america with 49 elements 
# remember, starts from element 0 and goes to n
states_of_america= [
    "Delaware",          # 1st
    "Pennsylvania",      # 2nd
    "New Jersey",        # 3rd
    "Georgia",           # 4th
    "Connecticut",       # 5th
    "Massachusetts",     # 6th
    "Maryland",          # 7th
    "South Carolina",    # 8th
    "New Hampshire",     # 9th
    "Virginia",          # 10th
    "New York",          # 11th
    "North Carolina",    # 12th
    "Rhode Island",      # 13th
    "Vermont",           # 14th
    "Kentucky",          # 15th
    "Tennessee",         # 16th
    "Ohio",              # 17th
    "Louisiana",         # 18th
    "Indiana",           # 19th
    "Mississippi",       # 20th
    "Illinois",          # 21st
    "Alabama",           # 22nd
    "Maine",             # 23rd
    "Missouri",          # 24th
    "Arkansas",          # 25th
    "Michigan",          # 26th
    "Florida",           # 27th
    "Texas",             # 28th
    "Iowa",              # 29th
    "Wisconsin",         # 30th
    "California",        # 31st
    "Minnesota",         # 32nd
    "Oregon",            # 33rd
    "Kansas",            # 34th
    "West Virginia",     # 35th
    "Nevada",            # 36th
    "Nebraska",          # 37th
    "Colorado",          # 38th
    "North Dakota",      # 39th
    "South Dakota",      # 40th
    "Montana",           # 41st
    "Washington",        # 42nd
    "Idaho",             # 43rd
    "Wyoming",           # 44th
    "Utah",              # 45th
    "Oklahoma",          # 46th
    "New Mexico",        # 47th
    "Arizona",           # 48th
    "Alaska",            # 49th
    "Hawaii"             # 50th
]

num_of_states = len(states_of_america) #this will give us the number of element in a list
# ATTENTION ! Starting from 1 

print(states_of_america[num_of_states])
```

<aside>
💡

By executing this code the console returns this error, we cannot access the element 50 of the list because the last element of the list is the one with index 49 

```bash
Traceback (most recent call last):
  File "/home/jose/Documents/100DaysOfPython/NestedList.py", line 59, in <module>
    print(states_of_america[num_of_states])
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
IndexError: list index out of range
```

</aside>
We can avoid the error by using this code. In this way the index will be shifted by -1 so the first will be 0 and the last 49 

```python
print(states_of_america[num_of_states - 1])
```

---

### Nested Lists

```python
#dirty_dozen_vegetables = [
#    "Strawberries",      # 1st
#    "Spinach",           # 2nd
#    "Kale",              # 3rd
#    "Nectarines",        # 4th (fruit, but often included)
#    "Apples",            # 5th (fruit, but often included)
#    "Grapes",            # 6th (fruit, but often included)
#    "Peppers (bell and hot)",  # 7th
#    "Celery",            # 8th
#    "Tomatoes",          # 9th
#    "Potatoes",          # 10th
#    "Cherries",          # 11th (fruit, but often included)
#    "Peaches"            # 12th (fruit, but often included)
#]

dirty_dozen_fruits = [
    "Strawberries",      # 1st
    "Nectarines",        # 2nd
    "Apples",            # 3rd
    "Grapes",            # 4th
    "Cherries",          # 5th
    "Peaches"            # 6th
]

dirty_dozen_vegetables = [
    "Spinach",           # 1st
    "Kale",              # 2nd
    "Peppers (bell and hot)",  # 3rd
    "Celery",            # 4th
    "Tomatoes",          # 5th
    "Potatoes"           # 6th
]

# In this way we have a list that contains two different list 
dirty_dozen = [dirty_dozen_fruits, dirty_dozen_vegetables]
print(dirty_dozen)
```

Output console. We can see the double [[ ]] each list is printed separately 

```bash
[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Cherries', 'Peaches'], ['Spinach', 'Kale', 'Peppers (bell and hot)', 'Celery', 'Tomatoes', 'Potatoes']]
```
---

### Exercise Day4

```python
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
```