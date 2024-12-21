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
#taking User input 
students = []
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("Enter the name of the student: ")
    marks_input = input(f"Enter marks for {name} separated by spaces: ")
    marks = list(map(int, marks_input.split()))
    students.append({"name": name, "marks": marks})
    
for student in students:
    total_marks = sum(student["marks"])
    percentage = (total_marks / (len(student["marks"]) * 100)) * 100
    student["percentage"] = percentage
    student["grade"] = determine_grade(percentage)

print("\nList of Students, Marks, Grades, and Percentages:")
for student in students:
    print(f"Name: {student['name']}, Marks: {student['marks']}, Grade: {student['grade']}, Percentage: {student['percentage']:.2f}%")
