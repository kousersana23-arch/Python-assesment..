
# Program 6: Function-Based Calculator

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Display calculator menu
print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user's choice
choice = input("Enter your choice (1-4): ")

# Perform the selected operation
if choice == "1":
    print("Result:", add(num1, num2))

elif choice == "2":
    print("Result:", subtract(num1, num2))

elif choice == "3":
    print("Result:", multiply(num1, num2))

elif choice == "4":
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice")
