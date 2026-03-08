while True:
    try:
        # Take input as a string
        user_input = input("Enter numbers separated by space: ")

        # Split → convert each item to int
        numbers = list(map(int, user_input.split()))

        print("Valid list:", numbers)
        break   # exit loop if successful

    except ValueError:
        print("Invalid input. Please enter only integers.")

    finally:
        print("Attempt finished")

