word = str(input("Enter a Word: "))
num = int(input("Enter a number: "))

x = word.split()[0]
y = x.capitalize()

print(x + str(num))
print(str(num) + x)
print(x.upper())
print(x.lower())
print(str(y) + str(y) + str(y) + str(y) + str(y))
print(str(y)*5)
