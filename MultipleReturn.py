def format_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "No string provided"# escape the function 
    
    # Convert string to title case 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    # THIS IS THE END OF THE FUNCTION
    return f'{formatted_f_name} {formatted_l_name}' 



print( format_name("jose", "SAVA"))