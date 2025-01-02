def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Is not possible to divide by 0")
        return
    else: 
        return n1 / n2 


# Add each function into a dictionary
operations = {
    # don't call the function with () 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def clear():
    print("\n" * 20 ) 