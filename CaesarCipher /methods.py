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
