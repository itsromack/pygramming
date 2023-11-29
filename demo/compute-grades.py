"""
Create a program that computes the final grade of a student
Assignment: 10%
Laboratory Activity: 30%
Quiz: 10%
Project: 20%
Major Exam: 30%
"""
print("Welcome to College ABCXYZ")
name = input("Enter your full name: ")

a1 = float(input("Assignment #1 Grade: "))
a2 = float(input("Assignment #2 Grade: "))
avg_assignments = (a1 + a2) / 2.0

lab1 = float(input("Laboratory Activity #1 Grade: "))
lab2 = float(input("Laboratory Activity #2 Grade: "))
lab3 = float(input("Laboratory Activity #3 Grade: "))
avg_lab = (lab1 + lab2 + lab3) / 3.0

q1 = float(input("Quiz #1 Grade: "))
q2 = float(input("Quiz #2 Grade: "))
avg_quiz = (q1 + q2) / 2.0

project = float(input("Project Grade: "))

midterm = float(input("Midterm Exam Grade: "))
finals = float(input("Finals Exam Grade: "))
avg_exam = (midterm + finals) / 2.0


def compute_final_grade(assignments, labs, quiz, proj, exam):
    total = 0
    total += assignments * 0.10         # total = total + (assignments * 0.10)
    total += labs * 0.30
    total += quiz * 0.10
    total += proj * 0.20
    total += exam * 0.30
    return total


def display_final_grade(student, grade):
    print("Hi", student, "your final grade is", grade)


def get_verdict(grade):
    if grade >= 75.0:
        return "PASSED"
    else:
        return "FAILED"


final_grade = compute_final_grade(avg_assignments, avg_lab, avg_quiz, project, avg_exam)
display_final_grade(name, final_grade)
print(get_verdict(final_grade))


# final_grade = (avg_assignments * 0.10) + (avg_lab * 0.30) + (avg_quiz * 0.10) + (project * 0.20) + (avg_exam * 0.30)
# print(name, " final grade is ", final_grade)
