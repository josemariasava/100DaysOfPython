#fruits = ["Apple", "Peach", "Pear"]
#
#for fruit in fruits:
#    print(fruit)

# List of a student score 
student_scores = [
    85, 92, 78, 88, 95, 76, 84, 91, 72, 89,
    80, 93, 67, 75, 90, 82, 88, 79, 85, 94
]


total_score = sum(student_scores) # calculate sum of all item of the list with sum() 
print(f"Total score with sum() function {total_score}")

print(f"Max value with max() function: {max(student_scores)}") 
#max() will return the maximum value item inside the list 

sum = 0
for score in student_scores:
    sum += score


print(f"Total score with for loop method {sum}")

max_score = 0
for score in student_scores: 
    if score > max_score:
        max_score = score

print(f"Max value with for loop method {max_score}")
