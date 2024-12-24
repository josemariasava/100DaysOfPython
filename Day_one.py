# Learning python in 100 days - day 1 

# '#' -->  write a comment

# STRING -->  composed by a set of character 
# print() --> used to print an output message to terminal 
# syntax :  print("your message")

# vid n. 6 
print("Day 1 of learning")
print("The funtion is declared like this: ")
print("print('your message'))")


# vid n.7 string manipulation 
# \n --> escape char 
print("Hello world! row 1 \nHello wordl! row 2") # \n escape char 

# concatenate strings 
# we can use the + operator to concatenate string into only one 
print("Hello" + " "+ "Josè") # concatenated 3 string into 1 

# vid n.9 Input Function 
# input() --> used to ask a promt for the user 
# syntax : input("prompt message for the user")

# input() is the first function executed and get the input in console
# then print() function will print the message with the name inserted by user in console
print("Hello! " + input("What is your name ? "))
# OUTPUT FROM TERMINAL ::
# What is your name ? Pippo 
# Hello! Pippo

# vid n.10 Input excercise 
# write a program that prints the number of char in a user's name 
# len() --> function that returns the number of items in an object

# with python we can write multiple function 
print( len(input("What is your name ? ")))

# 1 input()
# 2 len()
# 3 print()


# vid n.11 Python variables 
# = operator assign the value to a variable 
# variable is like a container were we store the data 
age = input("Insert your age: ") # input from the user will be stored inside the var age 
# with the variable we can use again the data because we stored in a memory location 
print("The age of the user is : " + age)
# used again the value age to print it 

# refactoring of exercise n.10 
name = input("What is your name ?")
lenght_name = len(name) # integer type
# we cannot concatenate integer and string with + operator 
print("Your name is composed by %s char" %(lenght_name))


# vid n.12 Variables excercise 
# write a program that switches the values stored in the variables A and B 

a = input("Input the value for a :")
b = input("Input the value for b :")

c = a # temporary variable to be enable to swap values 
a = b 
b = c 

print("Swap done!  a = %s b = %s"%(a,b))

# vid n.13 Variable naming 
# use talking name for the variable! Is to make the code readable by others
# one single unit --> user_name 
# number always at the end --> name1, name2 
# never use name of a function --> input : wrong name because same of a function 
