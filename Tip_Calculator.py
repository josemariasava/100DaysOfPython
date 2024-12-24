# 12% = 12/100 = 0.12 

print("Welcome to the tip calculator project!")

bill = float(input("What was the bill ? $ "))

tip = int(input("How much tip would you like to give? 10,12, or 15? "))

people = int(input("How many people to split the bill? "))


percentage = tip/100
total_tip = bill * percentage
total_bill = bill + total_tip


single_total = total_bill/people

print(f"Each person should pay: ${single_total}")