# Learning python in 100 days - day 3

#####################
#### PIZZA ORDER ####

# S = 15$ - Pepp +2 
# M = 20$ - Pepp +3
# L = 25$ - Pepp +3
print("Welcome to Python Pizza Deliveries!")

bill = 0 # start bill value from 0 

size = input("What size of pizza do you want ? S - M - L : ")



if(size == "S"):
    bill = 15
elif(size =="M"):
    bill = 20
elif(size =="L"):
    bill = 25

pepperoni = input("Pepperoni on your pizza ? Y or N : ") 
if(pepperoni == "Y"):
    if(size == "S"):
        bill += 2
    else: 
        bill += 3
else:
    extra_cheese = input("Extra Cheese on your pizza ? Y or N : ") # all size +1
    if(extra_cheese == "Y"):
        bill += 1 
 
        
print(f"Your final bill is: {bill}$") # print the final bill after users input 