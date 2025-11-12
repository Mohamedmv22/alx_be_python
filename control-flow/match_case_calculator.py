sum1 = int(input("Enter the first number: "))
sum2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    print(f"The result is: {sum1+sum2}")
elif operation == "-":
    print(f"The result is: {sum1-sum2}")
elif operation == "*":
    print(f"The result is: {sum1*sum2}")
elif operation == "/":
    print(f"The result is: {sum1/sum2}")
else:
    print("Sorry, check the operation and try again.")
