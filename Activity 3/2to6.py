def append():
    print("\n")
    a.append(input("Enter Something to append:"))

    for item in a:
        print(item)


def insert():
    nsrt = input("Enter something to insert: ")
    x = input("In what place do you want to insert a value, 5 as the highest? ")
    place = int(x) - 1
    a.insert(place, nsrt)

    print("\n")

    for item in a:
        print(item)


def remove():
    removeItem = input("What do you want to remove from the list ? ")
    a.remove(removeItem)
    for item in a:
        print(item)


a = [
    str(input("Enter Something: ")),
    str(input("Enter Something: ")),
    str(input("Enter Something: ")),
    str(input("Enter Something: ")),
    str(input("Enter Something: "))
]

print("\n")

for item in a:
    print(item)

print("\n")
for reversedItem in reversed(a):
    print(reversedItem)

print("\n What do you want to do?")
x = input("(A) Append (B) Insert (C) Remove \n")

if x.upper() == "A":
    append()
elif x.upper() == "B":
    insert()
elif x.upper() == "C":
    remove()
else:
    print("Invalid input. Terminating process.")
