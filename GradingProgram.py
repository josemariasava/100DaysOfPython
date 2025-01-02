student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

# Create an empty dictionary to store student grades
student_grades = {}

# Loop through the student_scores dictionary and assign grades
for student, score in student_scores.items():
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    # Add the student's grade to the student_grades dictionary
    student_grades[student] = grade

# Output the student_grades dictionary
print(student_grades)