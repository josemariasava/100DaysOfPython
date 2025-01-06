main_logo = """
▗▖ ▗▖▄    ▐▌   ▗▞▀▚▖ ▄▄▄     
▐▌ ▐▌▄    ▐▌   ▐▛▀▀▘█        
▐▛▀▜▌█    ▐▛▀▚▖▝▚▄▄▖█        
▐▌ ▐▌█ ▗▄▖▐▌ ▐▌              
      ▐▌ ▐▌                  
       ▝▀▜▌                  
      ▐▙▄▞▘                  
▗▖ ▄▄▄  ▄   ▄ ▗▞▀▚▖ ▄▄▄      
▐▌█   █ █ ▄ █ ▐▛▀▀▘█         
▐▌▀▄▄▄▀ █▄█▄█ ▝▚▄▄▖█         
▐▙▄▄▖                        
"""              
vs_logo = """
▄   ▄  ▄▄▄ 
█   █ ▀▄▄  
 ▀▄▀  ▄▄▄▀ ▄ 

"""

def format_data(account):
    """Takes the account data and 
    format the  data to be readable - Arg: the account record"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_data(user_guess, follower_a, follower_b):
    """Check if the choice of the user is right between the two follower data"""


    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"

def clear():
    print("\n" * 20)