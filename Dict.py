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