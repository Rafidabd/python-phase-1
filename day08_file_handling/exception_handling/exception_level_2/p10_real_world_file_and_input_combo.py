try:
    filename = input("Enter file name: ")
    n = int(input("Enter a number: "))

    result = 100 / n   # may raise ZeroDivisionError

    with open(filename, "a") as file:
        file.write(str(result) + "\n")

except ValueError:
    print("Invalid number entered")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("Data written successfully")

finally:
    print("Program finished")


    

    