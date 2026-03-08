try:
    f = input("Enter file name: ")
    n = int(input("Enter a number: "))   # ValueError possible

    result = 10 / n                      # ZeroDivisionError possible

    with open(f, "a") as file:           # Safe: creates file
        file.write(str(result) + "\n")

except ValueError:
    print("Invalid number input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("Operation successful")

finally:
    print("Execution finished")


        