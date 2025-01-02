### Functions with Outputs

```python
def my_function():
	result = 3*2
	
	return result # Output keyword -> output of the function 
```

```python
def format_name(f_name,l_name):
    # Convert string to title case 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    print(f'{formatted_f_name} {formatted_l_name}')

format_name("jose", "SAVA")
```

**Same code results with return statement inside the function** 

```python
def format_name(f_name,l_name):
    # Convert string to title case 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # THIS IS THE END OF THE FUNCTION
    return f'{formatted_f_name} {formatted_l_name}' 
    # THIS LINE OF CODE IS NEVER EXECUTED BECAUSE AFTER THE RETURN KEYWORD
    print("after return")

print( format_name("jose", "SAVA"))
```

**Exit the function with multiple return statement** 

```python
def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "No string provided"# escape the function 
    
    # Convert string to title case 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # THIS IS THE END OF THE FUNCTION
    return f'{formatted_f_name} {formatted_l_name}' 
```

**Function as input of another one**

```python
def function_1(text):
    return text + text 

def function_2(text):
    return text.title()

output = function_1("Hello")
print(output)

# Use the output of one function as input of another one
output2 = function_2(function_1("Hello"))
print(output2)
```

---

### Is leap year()

```python
def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2400))
print(is_leap_year(1989))
```

---

### What is a Docstring?

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes the **doc** special attribute of that object.

All modules should normally have docstrings, and all functions and classes exported by a module should also have docstrings. Public methods (including the **init** constructor) should also have docstrings. A package may be documented in the module docstring of the **init**.py file in the package directory.

String literals occurring elsewhere in Python code may also act as documentation. They are not recognized by the Python bytecode compiler and are not accessible as runtime object attributes (i.e. not assigned to **doc**), but two types of extra docstrings may be extracted by software tools:

> String literals occurring immediately after a simple assignment at the top level of a module, class, or __init__ method are called “attribute docstrings”.
String literals occurring immediately after another docstring are called “additional docstrings”.
> 

For consistency, always use """triple double quotes""" around docstrings. Use r"""raw triple double quotes""" if you use any backslashes in your docstrings.

### Python .__doc__  attribute

> Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their **doc** attribute. We can later use this attribute to retrieve this docstring.
> 

```python
def square(n):
    '''Take a number n and return the square of n.'''
    return n**2

print(square.__doc__)
```

```python
def function():
    """
    This is the doctring of a function, is the firts line of declaration of our function.
    Is helpful for documentation. 
    """

function()
```
---

### Calculator

**function.py**

Add each function inside a dictionary, in this way is more accessible each function 

```python
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Is not possible to divide by 0")
        return
    else: 
        return n1 / n2 

# Add each function into a dictionary
operations = {
    # don't call the function with () 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def clear():
    print("\n" * 20 ) 
```

**main.py**

Defined a function called calculator() and called inside itself make the recursion 

> Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
> 

```python
import function

def calculator():
    accumulate = True
    num1 = float(input("What is the first number?: ")) # cast the input to float type
    while accumulate:

        for symbol in function.operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: ")) # cast the input to float type

        result = function.operations[operation_symbol](num1,num2)

        choice = input(f"Type 'y' to continue calculationg with {result}, or 'n' to start a new calculation\n")

        if choice == "y":
            num1 = result
        else:
            accumulate = False
            function.clear() 
            calculator()

calculator()

```