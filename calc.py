# Calculator Program in Python

# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract two numbers
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide two numbers
def divide(x, y):
    # Check to prevent division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Display available operations to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Check if the choice is valid (between 1 and 4)
if choice in ('1', '2', '3', '4'):
    # Ask the user for input numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

else:
    # If the choice is invalid, show an error message
    print("Invalid input! Please choose a number between 1 and 4.")
