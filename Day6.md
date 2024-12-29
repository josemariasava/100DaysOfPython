### Functions

> Python Functions is a block of statements that return the specific task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
> 
> 
> Some Benefits of Using Functions: 
> 
> - Increase Code Readability
> - Increase Code Reusability
> 
> There are two different types of Functions: 
> 
> Built-in library function: These are Standard functions in Python that are available to use.
> 
> User-defined function: We can create our own functions based on our requirements.
> 
> In Python, you define a function with the `def` keyword, then write the function identifier (name) followed by parentheses and a colon.
> 

```python
def functionName():
    # What to make the function do
```

To call this function, write the name of the function followed by parentheses:

```python
myfunction()
```
#### Python Function Syntax with Parameters

```python
def function_name(parameter: data_type) -> return_type:
    """Docstring"""
    # body of the function
    return expression
```

##### Version 1 
In this snippet of code the data type of each argument is declared, as well the type of return data: int

```python
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
```

##### Version 2 
In this snippet the data type is not declared, but the return value is still type <int>

```python
def add(num1, num2):
    num3 = num1 + num2
    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")
print(type(ans))
```

```bash
# CONSOLE OUTPUT 
The addition of 5 and 15 results 20.
<class 'int'>
```
---
### Reborg Challenge

[Reeborg's World](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)

#### Solutiion for the Hurdless loop challenge

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# draw a square 
for step in range(1,7):
    jump()
```

---

### Indentation
[PEP 8 – Style Guide for Python Code | peps.python.org](https://peps.python.org/pep-0008/)

```python
def add(num1, num2):
    num3 = num1 + num2
    return num3
num4 #This line of code is not inside the function
```

<aside>
💡

- The first two print statements are indented by 4 spaces, so they belong to the if block.
- The third print statement is not indented, so it is outside the if block.

```python
if 10 > 5:
    print("This is true!")
    print("I am tab indentation")

print("I have no indentation")
```

</aside>

---

### While loop

> With the while loop we can execute a set of statements as long as a condition is true.
> 

```python
i = 1
while i < 6:
  print(i)
  i += 1
```

```python
# while something_is_true:
    #Do something

# While loop to take inputs from a user 
# stop the loop when user input 0 

n = int(input("Enter a number: ")) # ask the user and cast to int the input value 

while (n != 0):
    n = int(input("Enter zero to quit: "))
```

### Break statement

> With the break statement we can stop the loop even if the while condition is true:
> 

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
```