words = [
    str(input("Enter something: ")),
    str(input("Enter something: ")),
    str(input("Enter something: ")),
    str(input("Enter something: ")),
    str(input("Enter something: ")),
]

sortedWords = sorted(words)
reverseWords = sorted(sortedWords, reverse=True)

print(words)
print(sortedWords)
print(reverseWords)


