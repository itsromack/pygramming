print("College of Subic Montessori")
print("Dinalupihan Campus")
print("=============================")
print("Welcome to Simple Quiz")
print("=============================")
name = input("Please Enter your Complete Name: ")
ready = input("Are you ready to play the Quiz? (yes/no): ")

score = 0
total_questions = 3

def say_correct():
    print("Correct! :)")
    print("...")

def say_wrong():
    print("Wrong :(")
    print("...")

if ready.lower() == "yes":
    answer = input("Question #1: What is your favorite programming language? ")
    if answer.lower() == "python":
        score += 1
        say_correct()
    else:
        say_wrong()

    answer = input("Question #2: What's the first name of Python Programming Language's Inventor? ")
    if answer.lower() == "guido":
        score += 1
        say_correct()
    else:
        say_wrong()

    answer = input("Question #3: What is the year today? ")
    if int(answer) == 2023:
        score += 1
        say_correct()
    else:
        say_wrong()

print("===========================================")
print("Thank you for playing this small quiz game")
print("You got a score of", score, "out of", total_questions)
print("BYE", name, "!")
print("XXXXXXXXXXX END OF PROGRAM XXXXXXXXXXXXXXXX")
