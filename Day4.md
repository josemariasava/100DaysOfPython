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