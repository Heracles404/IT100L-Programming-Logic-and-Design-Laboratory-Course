import os


def registerOrOverwrite():
    print("Input Student Data: ")
    name = input("Name: ")
    program = input("Program: ")
    email = input("Email Address: ")
    gender = input("Gender: ")
    try:
        age = int(input("Age: "))
    except:
        print("Invalid input enter again: ")
        age = input("Age: ")
    birthday = input("Birthday: ")
    birthPlace = input("Place of Birth: ")
    civilStatus = input("Civil Status: ")
    nationality = input("Nationality: ")
    contact = [
        input("Mobile Number: "),
        input("Landline: "),
    ]
    address = [
        input("Present Address: "),
        input("Permanent Address: ")
    ]

    savePath = 'E:\MCL 3T\IT100L - A11\Projects\Finals'
    completeName = os.path.join(savePath, studentNumber + ".txt")
    data = open(completeName, "w")
    write = "\nName: " + name + "\nProgram: " + program + "\nE-mail: " + email + "\nGender: " + gender + "\nAge: " + str(
        age) + "\nBirthday: " + birthday + "\nBirth Place: " + birthPlace + "\nCivil Status: " + civilStatus + "\nNationality: " + nationality + "\nMobile Number: " + \
            contact[0] + "\nLandline; " + contact[1] + "\nPresent Address: " + address[0] + "\nPermanent Adress: " + \
            address[1]
    data.write(str(write))
    data.close()


def view():
    try:
        studentFile = open(studentNumber + ".txt")
        lines = studentFile.readlines()
        for line in lines:
            print(line)
        studentFile.close()
    except:
        print("Record not found.")


def delete():
    if os.path.exists(studentNumber + ".txt"):
        os.remove(studentNumber + ".txt")
    else:
        print("Student record doesn't exits.")


splash = input(
    "What do you want to do? \n A) Add New Record \n B) Edit/Overwrite a Record \n C) View Record \n D) Delete a record  \n >>")

if splash.upper() == "A":
    studentNumber = input("Enter Student Number: ")
    registerOrOverwrite()
elif splash.upper() == "B":
    studentNumber = input("Enter Student Number: ")
    registerOrOverwrite()
elif splash.upper() == "C":
    studentNumber = input("Enter Student Number: ")
    view()
elif splash.upper() == "D":
    studentNumber = input("Enter Student Number to Delete: ")
    delete()
else:
    print("Invalid input. Try again.")
    os.system("StudentsPersonalDataSheet.py")
    exit()

again = input("Do you want to select again? \n>>>")
if again.lower() in "y yes":
    os.system("StudentsPersonalDataSheet.py")
    exit()
elif again.lower() in "n no":
    exit()
else:
    print("Response not recognized. \nEnding process now.")
