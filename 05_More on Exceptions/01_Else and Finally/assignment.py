
number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a Number:"))
    number2 = int(input("Enter a Number:"))
except ValueError:
    print("An Input Was Not Correct")
else:
    print("No Value Error Detected")
finally:
    print("Values Taken Care Of")
try:
    number1 / number2
    Answer = number1 / number2
    print(Answer)
except ZeroDivisionError:
    print("That Number Is Not Divisible")
else:
    print("No Division Error Detected")
finally:
    print("Division Taken Care Of")