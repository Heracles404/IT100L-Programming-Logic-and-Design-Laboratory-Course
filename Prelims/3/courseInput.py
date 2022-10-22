courseCode1 = input("\nCourse Code 1: ")
courseUnits1 = input("Course Units 1: ")
while float(courseUnits1) < 0 or float(courseUnits1) > 5:
    courseUnits1 = input("Invalid input, try again. \n Course Units 1: ")
courseGrade1 = float(input("Course Grade 1: "))
while float(courseGrade1) % 0.25 != 0:
    courseGrade1 = float(input("Invalid input, try again. \n Course Grade 1: "))

courseCode2 = input("\nCourse Code 2: ")
courseUnits2 = input("Course Units 2: ")
while float(courseUnits2) < 0 or float(courseUnits2) > 5:
    courseUnits2 = input("Invalid input, try again. \n Course Units 2: ")
courseGrade2 = float(input("Course Grade 2: "))
while float(courseGrade2) % 0.25 != 0:
    courseGrade2 = float(input("Invalid input, try again. \n Course Grade 2: "))

courseCode3 = input("\nCourse Code 3: ")
courseUnits3 = input("Course Units 3: ")
while float(courseUnits3) < 0 or float(courseUnits3) > 5:
    courseUnits3 = input("Invalid input, try again. \n Course Units 3: ")
courseGrade3 = float(input("Course Grade 3: "))
while float(courseGrade3) % 0.25 != 0:
    courseGrade3 = float(input("Invalid input, try again. \n Course Grade 3: "))

courseCode4 = input("\nCourse Code 4: ")
courseUnits4 = input("Course Units 4: ")
while float(courseUnits4) < 0 or float(courseUnits4) > 5:
    courseUnits4 = input("Invalid input, try again. \n Course Units 4: ")
courseGrade4 = float(input("Course Grade 4: "))
while float(courseGrade4) % 0.25 != 0:
    courseGrade4 = float(input("Invalid input, try again. \n Course Grade : "))

courseCode5 = input("\nCourse Code 5: ")
courseUnits5 = input("Course Units 5: ")
while float(courseUnits5) < 0 or float(courseUnits5) > 5:
    courseUnits5 = input("Invalid input, try again. \n Course Units 5: ")
courseGrade5 = float(input("Course Grade 5: "))
while float(courseGrade5) % 0.25 != 0:
    courseGrade5 = float(input("Invalid input, try again. \n Course Grade 5: "))

courseCode6 = input("\nCourse Code 6: ")
courseUnits6 = input("Course Units 6: ")
while float(courseUnits6) < 0 or float(courseUnits6) > 5:
    courseUnits6 = input("Invalid input, try again. \n Course Units 6: ")
courseGrade6 = float(input("Course Grade 6: "))
while float(courseGrade6) % 0.25 != 0:
    courseGrade6 = float(input("Invalid input, try again. \n Course Grade 6: "))

tUnits = courseUnits1 + courseUnits2 + courseUnits3 + courseUnits4 + courseUnits5 + courseUnits6
gwa = ((float(courseGrade1)*float(courseUnits1)) + (float(courseGrade2)*float(courseUnits2)) + (float(courseGrade3)*float(courseUnits3)) + (float(courseGrade4)*float(courseUnits4)) + (float(courseGrade5)*float(courseUnits5)) + (float(courseGrade6)*float(courseUnits6))) / float(tUnits)

if float(gwa) <= 1.5 and float(courseGrade1) < 5 and float(courseGrade2) < 5 and float(courseGrade3) < 5 and float(courseGrade4) < 5 and float(courseGrade5) < 5 and float(courseGrade6) < 5:
    lister = str("President's Lister")
elif 1.5 > float(gwa) >= 1.75 and float(courseGrade1) < 5 and float(courseGrade2) < 5 and float(courseGrade3) < 5 and float(courseGrade4) < 5 and float(courseGrade5) < 5 and float(courseGrade6) < 5:
    lister = str("Dean's Lister")
elif 3 > float(gwa) > 1.75 and float(courseGrade1) < 5 and float(courseGrade2) < 5 and float(courseGrade3) < 5 and float(courseGrade4) < 5 and float(courseGrade5) < 5 and float(courseGrade6) < 5:
    lister = str("Parent's Lister")
else:
    lister = str("N/A")


