# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation as letters D, M, T, S: ")

# if (operation == "D"):
#     print(num1 / num2)
# elif (operation == "M"):
#     print(num1 * num2)
# elif (operation == "T"):
#     print(num1 + num2)
# elif (operation == "S"):
#     print(num1 - num2)
# else: 
#     print("Invalid operation")

#       choice = input("Do you want to continue (C) or quit (Q)? ").upper()

#     if choice != "C":
#         break
while True:
    # Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask for the operation
    operation = input("Choose an operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation."

    # Display the result
    print(f"Result: {result}")

    # Ask the user if they want to continue
    choice = input("Do you want to continue (C) or quit (Q)? ").upper()

    if choice != "C":
        break

