number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"The result is: {number1 + number2}")
    case "-":
        print(f"The result is: {number1 - number2}")
    case "*":
        print(f"The result is: {number1 * number2}")
    case "/":
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"The result is: {number1 / number2}")
    case _:
        print("Sorry, check the operation and try again.")

