#for number in range(a,b):
#   print (number)

# this will print the number in a range 1-9, the 10 is not included 
#for number in range(1,10):
#    print(number) 

# this will print the number in a range 1-11, the 11 is not included 
for number in range(1,11,3): # this will print by step 3 
    print(number) 


### GAUSS CHALLENGE 

total = 0
for gauss in range(1,101):
    total += gauss

print(f"GAUSS VALUE : {total}")