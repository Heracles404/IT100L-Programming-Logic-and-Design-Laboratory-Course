import studentDeet
import courseInput

print("\n Student Name: " + str(studentDeet.studentName.capitalize()))
print("Student Number: " + str(studentDeet.studentNumber))

print("\nCourse Code         Units         Grade")
print(str(courseInput.courseCode1.upper()) + "               " + str(courseInput.courseUnits1) + "            " + str(float(courseInput.courseGrade1)))
print(str(courseInput.courseCode2.upper()) + "               " + str(courseInput.courseUnits2) + "            " + str(float(courseInput.courseGrade2)))
print(str(courseInput.courseCode3.upper()) + "               " + str(courseInput.courseUnits3) + "            " + str(float(courseInput.courseGrade3)))
print(str(courseInput.courseCode4.upper()) + "               " + str(courseInput.courseUnits4) + "            " + str(float(courseInput.courseGrade4)))
print(str(courseInput.courseCode5.upper()) + "               " + str(courseInput.courseUnits5) + "            " + str(float(courseInput.courseGrade5)))
print(str(courseInput.courseCode6.upper()) + "               " + str(courseInput.courseUnits6) + "            " + str(float(courseInput.courseGrade6)))

print("\nTotal Units: " + str(courseInput.tUnits))
print("General Weighted Average: " + str(courseInput.gwa))
print("Lister Status: " + str(courseInput.lister))