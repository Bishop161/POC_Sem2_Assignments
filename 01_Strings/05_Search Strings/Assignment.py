text = input("Enter Some text:")

result = text.find("the")

if result == -1:
    print("The word is not in the string.")
else:
    print("The word is in the string.")
    print("It is located at", result)