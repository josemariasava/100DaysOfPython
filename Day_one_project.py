# 1 Create a greeting for your program 
# 2 Ask the user for the city that they grew up 
# 3 Ask the user for the name of a pet 
# 4 Combine the name of their city and pet and show them their band name 

# greetings
print("Welcome to band generator.")

# ask & store inout from user 
city = input("In wich city did you grow up ? ")
pet = input("What's your pet's name ? ")

#print final result 
band_name = print("The name of yor band could be : " + city + " " + pet)
# becasue all the variables are string we can concatenate it using the + operator