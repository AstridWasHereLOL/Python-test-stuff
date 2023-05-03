operation = input("What operation are you using? ")
num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

if operation == "addition":
    ans = (num1 + num2)
elif operation == "subtraction":
    ans = (num1 - num2)
elif operation == "multiplication":
    ans = (num1 * num2)
elif operation == "division":
    ans = (num1 / num2)
else:
    print("I don't know that operation type. Try again with no captials, no spaces, and the full name of the operation.")

print("The answer is " + str(ans) + ".")