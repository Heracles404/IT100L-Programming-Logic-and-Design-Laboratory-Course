name = input("Enter your name: ")

prelim = input("Enter your prelim exam score: ")
while float(prelim) > 100 or float(prelim) < 0:
    prelim = input("Enter your prelim exam score: ")

midterm = input("Enter your midterm exam score: ")
while float(midterm) > 100 or float(midterm) < 0:
    midterm = input("Invalid! Please enter a valid midterm exam score: ")

final = input("Enter your final exam score: ")
while float(final) > 100 or float(final) < 0:
    final = input("Invalid! Please enter a valid final exam score: ")


qOne = input("Enter quiz #1 score: ")
while float(qOne) > 50 or float(qOne) < 0:
    qOne = input("Invalid! Please enter a valid quiz score: ")

qTwo = input("Enter quiz #2 score: ")
while float(qTwo) > 50 or float(qTwo) < 0:
    qTwo = input("Invalid! Please enter a valid quiz score: ")

qThree = input("Enter quiz #3 score: ")
while float(qThree) > 50 or float(qThree) < 0:
    qThree = input("Invalid! Please enter a valid quiz score: ")


assignmentOne = input("Assignment #1 score: ")
while float(assignmentOne) > 25 or float(assignmentOne) < 0:
    assignmentOne = input("Invalid! Please enter a valid assignment score: ")

assignmentTwo = input("Assignment #2 score: ")
while float(assignmentTwo) > 25 or float(assignmentTwo) < 0:
    assignmentTwo = input("Invalid! Please enter a valid assignment score: ")

totalExam = ((float(prelim) + float(midterm) + float(final))/300)*60
totalQuiz = ((float(qOne) + float(qTwo) + float(qThree))/150)*30
totalAssignment = ((float(assignmentOne) + float(assignmentTwo))/50)*10

grade = float(totalExam) + float(totalQuiz) + float(totalAssignment)

if float(grade) > 96:
    finalGrade = 1.00
elif 96 <= float(grade) >= 91.51:
    finalGrade = 1.25
elif 91.50 <= float(grade) >= 87.01:
    finalGrade = 1.50
elif 87.00 <= float(grade) >= 82.51:
    finalGrade = 1.75
elif 82.50 <= float(grade) >= 78.01:
    finalGrade = 2.00
elif 78.00 <= float(grade) >= 73.51:
    finalGrade = 2.25
elif 73.50 <= float(grade) >= 69.01:
    finalGrade = 2.50
elif 69.0 <= float(grade) >= 64.51:
    finalGrade = 2.75
elif 64.50 <= float(grade) >= 60:
    finalGrade = 3.00
else:
    finalGrade = 5.00

if finalGrade <= 3:
    print("Hi " + name +"! Your final grade is " + str(grade) + "%. Your equivalent grade is " + str(finalGrade) + ". You PASSED the course!")
else:
    print("Hi " + name + "! Your final grade is " + str(grade) + "%. Your equivalent grade is " + str(finalGrade) + ". You FAILED the course!")



