def format_name(f_name,l_name):
    # Convert string to title case 
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f'{formatted_f_name} {formatted_l_name}'


print( format_name("jose", "SAVA"))


def function_1(text):
    return text + text 

def function_2(text):
    return text.title()

output = function_1("Hello")
print(output)

# Use the output of one function as input of another one
output2 = function_2(function_1("Hello"))
print(output2)
