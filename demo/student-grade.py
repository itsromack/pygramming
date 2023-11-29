print("SCHOOL NAME ABCXYZ GRADING PROGRAM")
name = input("Enter student's full name: ")

# Get student's grades
assignment1 = float(input("Enter grade for Assignment #1: (50 - 100) "))
assignment2 = float(input("Enter grade for Assignment #2: (50 - 100) "))
assignment3 = float(input("Enter grade for Assignment #3: (50 - 100) "))
lab1 = float(input("Enter grade for Laboratory Activity #1: (50 - 100) "))
lab2 = float(input("Enter grade for Laboratory Activity #2: (50 - 100) "))
lab3 = float(input("Enter grade for Laboratory Activity #3: (50 - 100) "))
quiz1 = float(input("Enter grade for Quiz #1: (50 - 100) "))
quiz2 = float(input("Enter grade for Quiz #2: (50 - 100) "))
project = float(input("Enter grade for the Project: (50 - 100) "))
midterm = float(input("Enter grade for Midterm Exam: (50 - 100) "))
final = float(input("Enter grade for Final Exam: (50 - 100) "))

# Display the percentage distribution
print("Assignment: 10%")
print("Laboratory Activity: 20%")
print("Quiz: 20%")
print("Project: 20%")
print("Major Exam: 30%")

# Compute the grades
avg_assignment = (assignment1 + assignment2 + assignment3) / 3.0
avg_lab = (lab1 + lab2 + lab3) / 3.0
avg_quiz = (quiz1 + quiz2) / 2.0
avg_exam = (midterm + final) / 2.0

# Display student's grades
print('=============================')
print(name, " grades")
print("Assignment: ", avg_assignment)
print("Laboratory Activity: ", avg_lab)
print("Quiz: ", avg_quiz)
print("Project: ", project)
print("Major Exam: ", avg_exam)

# Compute and display the final grade
final_grade = (avg_assignment * .01) + (avg_lab * 0.2) + (avg_quiz * 0.2) + (project * 0.2) + (avg_exam * 0.3)
print(name, " final grade is ", final_grade)
if final_grade >= 75:
    print("Congratulations!", name, " you did great")
else:
    print("You need to keep improving ", name)
