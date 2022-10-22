numbers = [
    int(input("Enter a number: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
    int(input("Enter a number again: ")),
]
x = sorted(numbers)
xReverse = sorted(numbers, reverse=True)

print(numbers)
print(x)
print(xReverse)

print("Average: " + str(sum(numbers)/len(numbers)))
print("Lowest Input: " + str(x[0]))
print("Highest Input: " + str(x[9]))
