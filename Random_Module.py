# Deterministic: perform repetitive acion in predictable way 

### https://docs.python.org/3/library/random.html ### 
#Functions for integers
#random.randrange(stop)
#random.randrange(start, stop[, step])
#   Return a randomly selected element from range(start, stop, step).

import random #random module 
import my_module 

a = random.randint(1,100); #Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

print(f'The random integrer generated is {a}')

#OUTPUT CONSOLE 
# The random integrer generated is n where n is in the range 1,100 

b = random.random() # Return the next random floating-point number in the range 0.0 <= X < 1.0

print(f'The random floating point using random() is {b}')

# Return a random floating-point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
c = random. uniform(0,100)

print(f'The random floating point using uniform() is {c}')