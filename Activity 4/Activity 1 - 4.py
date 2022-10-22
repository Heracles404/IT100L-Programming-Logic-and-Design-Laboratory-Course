def thisMain():
    age = input("Enter your age:")
    print("Hello " + nameInput.name + " you are currently " + age + " years old.")

    birthYear = 2021 - int(age)
    print("You were born on " + str(birthYear))

    year = (100 - int(age)) + 2021
    print("By year " + str(year) + " you will be 100 years old.")

    someYears = year - 2021
    print("You will have to wait " + str(someYears) + " years to be 100 years old.")


import nameInput

x = nameInput.name
while x.upper() != "END":
    thisMain()
    x = input("Enter your complete Name:")
