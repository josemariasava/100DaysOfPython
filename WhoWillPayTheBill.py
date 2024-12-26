#prit randomly one elements of the list 
import random

friends = ["Alice", "Bob", "Charles", "David", "Emanuel"]
#INDEX      #0      #1      #2          #3      #4

# SOLUTION1 - generate a random number and print the element 
random_item = random.randint(0,4) #Generate random number with range 0-4 

print("SOLUTION 1")
print(friends[random_item])

# SOLUTION2 - access randomly the item inside the list with choice() 
# random.choice(seq)
#    Return a random element from the non-empty sequence seq. If seq is empty, raises 

print("\nSOLUTION 2")
print(random.choice(friends))

