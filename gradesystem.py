def determine_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

def sum(marks):
    total = 0
    for i in range(len(marks)):
        total += marks[i]
    return total
#you have to take student name and marks from user dynamically. Do it and update the code
students = [
    {"name": "Ram", "marks": [75, 85, 95, 58, 80]},
    {"name": "Sam", "marks": [68, 86, 77, 68, 69]},
    {"name": "Laxman", "marks": [78, 85, 95, 65, 79]},
    {"name": "Bharat", "marks": [90, 95, 86, 78, 88]}
]

for student in students:
    total_marks = sum(student["marks"])
    percentage = (total_marks / (len(student["marks"]) * 100)) * 100
    student["percentage"] = percentage
    student["grade"] = determine_grade(percentage)

print("\nList of Students, Marks, Grades, and Percentages:")
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}, Percentage: {student['percentage']:.2f}%")
