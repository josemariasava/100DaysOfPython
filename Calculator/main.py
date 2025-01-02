import function

def calculator():
    accumulate = True
    num1 = float(input("What is the first number?: ")) # cast the input to float type
    while accumulate:

        for symbol in function.operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: ")) # cast the input to float type

        result = function.operations[operation_symbol](num1,num2)

        choice = input(f"Type 'y' to continue calculationg with {result}, or 'n' to start a new calculation\n")

        if choice == "y":
            num1 = result
        else:
            accumulate = False
            function.clear() 
            calculator()


calculator()

