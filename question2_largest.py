
# Program 2: Largest of Three Numbers

# Take three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Compare the three numbers
if a >= b and a >= c:
    print("Largest number is:", a)

elif b >= a and b >= c:
    print("Largest number is:", b)

else:
    print("Largest number is:", c)
