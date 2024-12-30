import methods

run = True
print(methods.logo)
# While loop to let the user choose whether to continue or not
while (run == True):
    # Manage all the I/O in lower case 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    message = input("Typer your message: \n").lower()

    key = int(input("Type the key number: \n"))


    methods.caesar(word=message,shift=key,direction=direction)


    choice = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()
    

    # Stop the running of program 
    if (choice == "no"):
        run = False
        print("Goodbye")



