print("Enter only positive integers:")
numbers = [
    int(input("Enter a number: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: "))
]

while numbers[0] < 0 or numbers[1] < 0 or numbers[2] < 0 or numbers[3] < 0 or numbers[4] < 0:
    print("You've entered invalid value(s), try again!")
    numbers = [
        int(input("Enter a number: ")),
        int(input("Enter a number again: ")),
        int(input("Enter a number again: ")),
        int(input("Enter a number again: ")),
        int(input("Enter a number again: "))
    ]

x = sorted(numbers)
xReverse = sorted(numbers, reverse=True)

print(numbers)
print(x)
print(xReverse)

print("Average: " + str(sum(numbers)/len(numbers)))
print("Highest Input: " + str(x[4]))
print("Lowest Input: " + str(x[0]))
