# Name of the class is in PascalCase 
class User: 

    # Constructor of our function - called any tyme an object of this class is created
    def __init__(self, username, user_id): 
        self.username = username # attribute initialized
        self.id = user_id # attribute initialized
        self.followers = 0 # is an attribute but not in the constructor, so when the object is initialized is not necessary to pass this attribute
        self.following = 0

    def follow(self,user): # self as first parameter, in this way the method knows wich object that called it 
        user.followers += 1 # this its done to the user given as argument
    
        self.following += 1 # this affects the object itself


# Name of the function in camelCase
def myFunction():
    pass # no method or content for the moment

var_one = 1 # Name of the var in snake_case 

user_one = User("Pippo","001")
user_two = User("Angela", "002")

user_one.follow(user_two)

print(f"User {user_one.id} followers: {user_one.followers} \nUser one following: {user_one.following}")
print(f"User {user_two.id} followers: {user_two.followers} \nUser one following: {user_two.following}")