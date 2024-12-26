### IF Statement

> if statement is the most simple decision-making statement. If the condition evaluates to True, the block of code inside the if statement is executed.
> 

```python
i = 10

 # Checking if i is greater than 15
if (i > 15):
    print("10 is less than 15")
    
print("I am Not in if")
```

### IF…ELSE Statement

> if…else statement is a control statement that helps in decision-making based on specific conditions. When the if condition is False. If the condition in the if statement is not true, the else block will be executed.
> 

```python
i = 20

 # Checking if i is greater than 0
if (i > 0):
    print("i is positive")
else:
    print("i is 0 or Negative")

### IF ELSE in one  line 

number = -2

# Ternary conditional to check if number is positive or negative
result = "Positive" if number >= 0 else "Negative"
print(result)
```


### **if…elif…else Statement**

> if-elif-else statement in Python is used for multi-way decision-making. This allows you to check multiple conditions sequentially and execute a specific block of code when a condition is True. If none of the conditions are true, the else block is executed.
> 


### **Nested If Else Statement**

> Nested if…else statement occurs when if…else structure is placed inside another if or else block. Nested If..else allows the execution of specific code blocks based on a series of conditional checks.
> 

```python
i = 10
if (i == 10):
  
    #  First if statement
    if (i < 15):
        print("i is smaller than 15")
        
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
        
else:
  print("i is not equal to 10")
```

### Bitwise AND Operator

> Python Bitwise AND (&) operator takes two equal-length bit patterns as parameters. The two-bit integers are compared. If the bits in the compared positions of the bit patterns are 1, then the resulting bit is 1. If not, it is 0.
> 

```python
a = 10
b = 4

# Print bitwise AND operation
print("a & b =", a & b)

#OUTPUT 
# a & b = 0
```

### Bitwise XOR Operator

> The Python Bitwise XOR (^) Operator also known as the exclusive OR operator, is used to perform the XOR operation on two operands. XOR stands for “exclusive or”, and it returns true if and only if exactly one of the operands is true. In the context of bitwise operations, it compares corresponding bits of two operands. If the bits are different, it returns 1; otherwise, it returns 0.
> 

```python
a = 10
b = 4

# print bitwise XOR operation
print("a ^ b =", a ^ b)

#OUTPUT 
# a ^ b = 14
```

### Bitwise OR Operator

> The Python Bitwise OR (|) Operator takes two equivalent length bit designs as boundaries; if the two bits in the looked-at position are 0, the next bit is zero. If not, it is 1.
> 

```python
a = 10
b = 4

# Print bitwise OR operation
print("a | b =", a | b)

#OUTPUT 
# a | b = 14
```

### **Bitwise NOT Operator**

> The preceding three bitwise operators are binary operators, necessitating two operands to function. However, unlike the others, this operator operates with only one operand.
> 
> 
> Python Bitwise Not (~) Operator works with a single value and returns its one’s complement. This means it toggles all bits in the value, transforming 0 bits to 1 and 1 bits to 0, resulting in the one’s complement of the binary number.
> 

```python
a = 10
b = 4

# Print bitwise NOT operation
print("~a =", ~a)
```