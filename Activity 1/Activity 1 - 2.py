firstName = str(input("Enter your first name: ").capitalize())
middleName = str(input("Enter your middle name: ").capitalize())
lastName = str(input("Enter your surname: ").capitalize())
spc = " "

print("Hello " + firstName + spc + middleName + spc + lastName)
print("Hello " + firstName + spc + middleName[0] + spc + lastName)
