# Learning python in 100 days - day 3

####################
#### IF / ELSE  #### 

# if condition: 
#   do this
# else:
#   do other stuff

# print("Welcome to the rollercoaster!!")
# height = int(input("Enter your height in cm:  ")) # casting input from stringn to int type 

# if(height>=120):
#     print("You can ride the rollercoaster")
# else:
#     print("Go home and grow")


#########################
#### MODULO OPERATOR #### 

# binary operator - gives back the remainder after the division 

# x = 10 % 3 
# print(x) # result will be 1 : 10 / 3 = 3 with 1 remaining 

# check if the number is odd or even 
# even number 12 % 2 == 0 
# odd number 7 % 2 == 

# number = int(input("Insert the number to be checked "))

# if(number%2==0):
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd")


############################
#### NESTED IF AND ELIF #### 

# if condition: 
#     if another_condition: 
#         do this 
#     else 
#         do this 
# else: 
#     do this

# print("Welcome to the rollercoaster!!")
# height = int(input("Enter your height in cm:  ")) # casting input from stringn to int type 
# age = int(input("Enter your age : "))

# if (height>=120):
#     print("You can ride the rollercoaster")
#     if(age<=12):
#         print("Pay 5$ ticket")
#     elif(age<=18):                      #elif statement - we can use has many elif we want 
#         print("Pay 7$ ticket ")
#     else: 
#         print("Pay 12$ ticket")
# else:
#     print("Go home and grow")


###############################
#### MULTIPLE IF STATEMENT ####

# if cond1: 
#     do A
# if cond2: 
#     do B
# if cond3: 
#     do C

# print("Welcome to the rollercoaster!!")
# height = int(input("Enter your height in cm:  ")) # casting input from stringn to int type 
# age = int(input("Enter your age : "))
# bill = 0

# if (height>=120):
#     print("You can ride the rollercoaster")
#     if(age<=12):
#         print("Child Pay 5$ ticket")
#         bill = 5
#     elif(age<=18):                      #elif statement - we can use has many elif we want 
#         print("Youth Pay 7$ ticket ")
#         bill = 7 
#     else: 
#         print("Adult Pay 12$ ticket")
#         bill = 12 
    
#     photo = input("Do you want a photo?Y for yes | N for no ")
#     if(photo=="Y"):
#         bill += 3
#     print(f"your final bill is : ${bill}")
# else:
#     print("Go home and grow")
    

###########################
#### LOGICAL OPERATORS ####

# if condition1 & condition2 & condition3:
#     do this
# else 
#     do this 

# AND : A and B 
# OR  : A or B 
# NOT : not

print("Welcome to the rollercoaster!!")
height = int(input("Enter your height in cm:  ")) # casting input from stringn to int type 
age = int(input("Enter your age : "))
bill = 0

if (height>=120):
    print("You can ride the rollercoaster")
    if(age<=12):
        print("Child Pay 5$ ticket")
        bill = 5
    elif(age<=18):                      #elif statement - we can use has many elif we want 
        print("Youth Pay 7$ ticket ")
        bill = 7 
    elif(age >= 45 and age <=55):  # we can write also in this way :: 45<= age <= 55 
        print("Have a free ride")
    else: 
        print("Adult Pay 12$ ticket")
        bill = 12 
    
    photo = input("Do you want a photo?Y for yes | N for no ")
    if(photo=="Y"):
        bill += 3
    print(f"your final bill is : ${bill}")
else:
    print("Go home and grow")