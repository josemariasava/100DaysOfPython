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
