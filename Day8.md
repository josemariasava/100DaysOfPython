### Functions with inputs

```python
def my_function(some args):
		#Do this
		#Then this 
		#Final instruction 
```

#### Examples

```python
def greet():
    print("Hello ")
    print("How do you do? ")
    print("Isn't the weather nice? ")

# call the funztion 
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}" )

greet_with_name("Josè")
```
---

### **Keyword and Positional Argument in Python**

> **Keyword-only**
> 
> 
> arguments mean whenever we pass the arguments(or value) by their  parameter names at the time of calling the function in Python in which if you change the position of arguments then there will be no change in the output.
> 
> **Benefits of using Keyword arguments over positional arguments**
> 
> - On using keyword arguments you will get the
> correct output because the order of argument doesn’t matter provided the logic of your code is correct. But in the case of positional arguments, you will get more than one output on changing the order of the
> arguments.
> 
> ```python
> def nameAge(name, age):
>     print("Hi, I am", name)
>     print("My age is ", age)
> 
> nameAge(name="Prince", age=20)
> 
> nameAge(age=20, name="Prince")
> ```
> 
> ```bash
> # CONSOLE OUTPUT
> Hi, I am Prince
> My age is  20
> Hi, I am Prince
> My age is  20
> ```
> 
> **Position-only**
> 
> arguments mean whenever we pass the arguments in the order we have  defined function parameters in which if you change the argument position then you may get the unexpected output. We should use positional  Arguments whenever we know the order of argument to be passed. So now, we will call the function by using the position-only arguments in two ways and In both cases, we will be getting different outputs from which one will be correct and another one will be incorrect.
> 
> ```python
> def nameAge(name, age):
>     print("Hi, I am", name)
>     print("My age is ", age)
> 
> # You will get correct output because argument is given in order
> print("Case-1:")
> nameAge("Prince", 20)
> # You will get incorrect output because argument is not in order
> print("\nCase-2:")
> nameAge(20, "Prince")
> ```
> 
> ```bash
> # CONSOLE OUTPUT
> Case-1:
> Hi, I am Prince
> My age is  20
> 
> Case-2:
> Hi, I am 20
> My age is  Prince
> ```
>
---

### Caesar Cipher

> The Caesar cipher is the simplest and oldest method of cryptography. The Caesar cipher method is based on a mono-alphabetic cipher and is also called a shift cipher or additive cipher. Julius Caesar used the shift cipher (additive cipher) technique to communicate with his officers. For this reason, the shift cipher technique is called the Caesar cipher. The Caesar cipher is a kind of replacement (substitution) cipher, where all letter of plain text is replaced by another letter.
> 
> 
> Let's take an example to understand the Caesar cipher, suppose we are shifting with 1, then A will be replaced by B, B will be replaced by C, C will be replaced by D, D will be replaced by C, and this process continues until the entire plain text is finished.
> 
> Caesar ciphers is a weak method of cryptography. It can be easily hacked. It means the message encrypted by this method can be easily decrypted.
> 

**Method.py**

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# a = 0         | z = 25 

#index() --> The index() method returns the position at the first occurrence of the specified value.

logo = '''          
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''

def encrypt(word,shift):

    encrypted_word = "" # Empty string 
    for char in word:

        if char.islower():
            # Find the index of the character in the alphabet list
            index = alphabet.index(char)
            # Calculate the new shifted index and apply modulo 26 to wrap around
            new_index = (index+shift) % len(alphabet)

            new_char = alphabet[new_index]
            encrypted_word += new_char
        else:
            #Safety first ! Non-alphabetic characters (spaces, punctuation) are not changed
            encrypted_word += char

    return encrypted_word # return the encrypted word

def decrypt(word,shift):
    
    decrypted_word = "" # Empty string 

    for char in word:
        if char.islower():
            index = alphabet.index(char)
            new_index = (index-shift) % len(alphabet)

            new_char = alphabet[new_index]
            decrypted_word += new_char
        else:
            #Safety first ! Non-alphabetic characters (spaces, punctuation) are not changed
            decrypted_word += char

    return decrypted_word # return the decrypted word

def caesar(word,shift,direction):
    
    output_word = ""
    if direction == "decode":
        shift *= -1 
    for char in word:
        if char in alphabet:
            current_index = alphabet.index(char)
            new_index = (current_index+shift) % len(alphabet)
            output_word += alphabet[new_index]
        else:
            output_word += char
    
    print(f"Here is the {direction}d result: {output_word}")

```

Main.py

```python
import methods

run = True
print(methods.logo)
# While loop to let the user choose whether to continue or not
while (run == True):
    # Manage all the I/O in lower case 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    message = input("Typer your message: \n").lower()

    key = int(input("Type the key number: \n"))

    methods.caesar(word=message,shift=key,direction=direction)

    choice = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    

    # Stop the running of program 
    if (choice == "no"):
        run = False
        print("Goodbye")
```