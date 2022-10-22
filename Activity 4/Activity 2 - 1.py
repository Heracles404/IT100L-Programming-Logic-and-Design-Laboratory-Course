def thisMain():
    birthYear = input("Enter your birth year: ")
    ageA = 2022 - int(birthYear)
    ageB = 2016 - int(birthYear)
    year = int(birthYear) + 18

    if int(ageB) >= 18:
        print("Hi " + nameInput.name.capitalize() + ", you can vote for 2016 Presidential Elections.")
    elif int(ageA) >= 18 and ageB <= 18:
        print("Hi " + nameInput.name.capitalize() + ", you can vote for 2022 Presidential Elections.")
    else:
        print("You cannot vote yet for both elections. Please register on year " + str(year) + ".")


import nameInput

x = nameInput.name
while x.upper() != "END":
    thisMain()
    x = input("Enter your complete Name:")
