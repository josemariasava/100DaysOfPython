# Learning python in 100 days - day 2 

####################
#### DATA TYPES #### 

# print(len(123490)) # error, we cannot use the len() function for an integer value 

# STRING --> string of char "Hello" 
              #everything inside the "" is a string in python 


# SUBSCRIPTING --> used to retrieve a single element 
print("Hello"[0]) # it will print the H char because is the char in position 0 

print("Hello"[-1]) # in this way we weill access to the last char of the string, using -n we access the char in opposite way
print("Hello"[-2]) # this will print the char in position 4 that is l 


# INTEGER --> whole number, without any decimal places 
print(123 + 345) # calculation, the number are actual integer values

# Large integers --> 342,654,896 (comma to split and understand how big is the number)
                #    in python we can replace with _ : 342_654_896
print(342_654_896) # output from the console will be : 342654896

# FLOAT --> floating point number 3.14159 has a decimal place 
print(3.14159) # float value 

#BOOLEAN --> true or false / 0-1 True / False always with capital letter 
print(True)
print(False)

########################################
#### TYPE ERROR-CHECKING-CONVERSION #### 

print(type("Hello")) # type() function gives back the data type on any kind of data 
# output from the terminal : <class 'str'>

a = 10
print(type(a)) # output from the terminal : <class 'int'>

#### CAST TYPE #### 
int("123") #builtin function --> cast the value from string to int type 

# sometimes you can convert everything into another type 
# example int("ABC")
# output : ValueError: invalid literal for int() with base 10: 'ABC'
# int() --> convert to int 
# float() --> --> convert to flot
# str() --> convert to string  
# bool() --> convert to boolean 


########################################
#### MATEMATICAL OPERATIONS #### 
print(120+120)
print(8-2)
print(10*2)
# this is an implicit type casting 
print(6/3) # will give you a float value - in this case 2.0
print(6//3) # this operation gives an integer value
# just remove the decimal place 
print(2**2) # raise the number - to calculate the power of a number 

# in python math operation is executed with a certain priority 
# first * / then - + 
# PEMDAS --> Parentheses, Exponents, Multiplication/Disvision, Addition/subtraction 

print( 3 * 3 + 3 / 3 - 3 ) # will be print 7 

#order : 3 * 3  = 9
#        3 / 3  = 1 
#        10 - 3 = 7 

print(3 * (3+3) / 3 -3 ) # will be print 3 

#order : (3+3) = 6
#        6 * 3 = 18 
#        18 / 3 = 6 
#        6 - 3 = 3 


########################################
#### NUMBER MANIPULATION & FSTRING #####

bmi = 84/ (1.65 ** 2)

print(bmi) # output : 50.909090909090914

print(round(bmi)) # output : 31 
# round() function will round up or down the number given depending on the first decimal place value 

print(round(bmi,3)) # output : 30.854
# the second parameter is the number of decimal place that we want to considere for rounding


#### ASSIGNMENT OPERATOR 
# += will add the number on the right to the original value of the variable 
# on the left and assign the ne value to the variable 

var = 1 
var+=10
print(var) # output : 11 

var -= 2 
print(var) # output : 9

#### F-STRINGS
# In python we can use f-strings to insert a variable or an expression into a string
score = 0
height = 1.6
win = True 

print(f"The score is: {score} the height : {height} the win : {win}")








