operation = input("What operation are you using? ")
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

if operation == "addition":
    print(num1 + num2)
elif operation == "subtraction":
    print(num1 - num2)
elif operation == "multiplication":
    print(num1 * num2)
elif operation == "division":
    print(num1 / num2)
else:
    print("I don't know that operation type. Try again with no captials, no spaces, and the full name of the operation.")