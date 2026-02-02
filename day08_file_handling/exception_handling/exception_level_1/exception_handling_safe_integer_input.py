# Safe integer input
while True:
    try:
        n1 = int(input("Please enter your first number: "))
        n2 = int(input("Please enter your second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")

# Operation selection
op = input("Enter operation (addition/subtraction/multiplication/division): ")

if op == "addition":
    print("Result:", n1 + n2)

elif op == "subtraction":
    print("Result:", n1 - n2)

elif op == "multiplication":
    print("Result:", n1 * n2)

elif op == "division":
    try:
        print("Result:", n1 / n2)
    except ZeroDivisionError:
        print("Cannot divide by zero")

else:
    print("Invalid operation")


    



