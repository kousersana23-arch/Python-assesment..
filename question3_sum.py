
# Program 3: Sum of Numbers from 1 to N

# Take a positive integer from the user
n = int(input("Enter a positive number: "))

# Create a variable to store the sum
total = 0

# Loop from 1 to n
for i in range(1, n + 1):

    # Add each number to total
    total = total + i

# Print the final sum
print("Sum of numbers from 1 to", n, "is:", total)
