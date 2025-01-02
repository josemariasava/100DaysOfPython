> Dictionaries are used to store data values in key:value pairs.
> 
> 
> A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
> 
> - The values in dictionary items can be of any data type:
> - To determine how many items a dictionary has, use the `len()` function
> - It is also possible to use the dict() constructor to make a dictionary
> 
> ```python
> thisdict = dict(name = "John", age = 36, country = "Norway")
> ```
> 

**Dive in dictionary**

```python
thisdict =	{
  #key   :  value 
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
print(thisdict) # Print all the dict 

print(thisdict["brand"]) # Access the element of a dictionary by its key 
# this line will give the value "Ford "

# This will add to the end of dict a new key with its value 
thisdict["Name"] = "Josè" 
        # KEY       VALUE

# EMPTY DICT
empty_dict = {}

# WIPE AN EXISTING DICT 
thisdict = {} # clean all the content of a dict 

# EDIT THE CONTENT OF A DICT 
thisdict["brand"] = "MY NEW VALUE"

# LOOP THROUGH A DICT - 
for key in thisdict:
    print(key) # this code just print the key 
    print(thisdict[key]) # this print the value of the key inside the dict
```
**Exercise 9**

```python
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to store student grades
student_grades = {}

# Loop through the student_scores dictionary and assign grades
for student, score in student_scores.items():
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    # Add the student's grade to the student_grades dictionary
    student_grades[student] = grade

# Output the student_grades dictionary
print(student_grades)
```

---

### NESTING

{

**Key** : **Value**,

**Key2** : **Value2**,

**Key3** : **[List]**, —> Listed nested inside a dict 

**Key4** : **{Dict}** —> ****Dict nested inside a dict

}

```python
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary 
travel_log_list = {
    "France": ["Paris", "Lille", "Dijon", "Touluse"], # List
    "Germany": ["Berlin", "Amburg", "Frankfurt"] 
}

# Print Lille - accessing list inside dict 
print(travel_log_list["France"][1]) # this will output the value Lille

# Create a nested list 
nested_list = ["A", "B", ["C","D"]]
#print D - accessing item inside nested list 
print(nested_list[2][1]) # this will output the value D - Is like a matrix of data - 2D array

# Nested Dict in Dictionary
travel_log_dict = {
    "France": {
        "cities": ["Paris", "Lille", "Dijon", "Touluse"],
        "num_visited": 8,
    },
    "Germany": {
        "cities": ["Berlin", "Amburg", "Frankfurt"],
        "num_visited": 5,
    }
}

# Print Frankfurt 
print(travel_log_dict["Germany"]["cities"][2]) # this will output Frankfurt 

```
---

### Blind Auction

function.py

```python
# Definde logo 
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Add bid 
def add_bid(dict):

    #Ask the user for key and value 

    name = input("What is your name?: ") # key 
    price = int(input("What is your bid?: $ ")) # value 

    dict[name] = price

    return dict

# find best bid 
def find_best_bid(dict):
    highest = 0 
    winner = ""
    for bid in dict:
        bid_price = dict[bid]
        if bid_price > highest: 
            highest = bid_price
            winner = bid
    print(f'The winners is {winner} with a bid of ${highest}')

# Clear the console by printing 15 new line
def clear():
    print("\n" * 15)
```

main.py

```python
import function

# print the logo 
print(function.logo)

#Define empty dictionary and bool value to run/stop the code execution 

bids = {} # empty dict 
run = False # bool var 

# while loop 
while not run:
    # call add_bidd from function.py 
    function.add_bid(bids)

    # Ask if continue with another bid 
    bid_continue = input("Are there any other bidders? Type 'yes or no' \n").lower()

    if bid_continue == 'no':
        run = True
        function.find_best_bid(bids)
    elif bid_continue == "yes":
        function.clear()
```