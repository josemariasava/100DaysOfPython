# Learning python in 100 days - day 3

print("Welcome to Treasure Island.Your mission is to find the treasure")

step1 = input("left or right? ").lower()

if (step1 == "left"):
    # continue 
    step2 = input(" Do you want to swim or wait ? ").lower()
    if(step2 == "wait"):
        #continue 
        step3 = input("Wich door do you want to open? Red - Blue - Yellow ? ").lower()
        if(step3 == "red"):
            print("It's full of fire. Game Over!")
        elif(step3 == "blue"):
            print("Yoi have been eaten by beasts. Game Over!")
        elif(step3 == "yellow"):
            print("You win the treasure!!")
        else:
            print("Game Over!!")
    else: 
        print("You were attacked by trout.Game Over!")
else:
    print("You fall into a hole.Game Over!")
