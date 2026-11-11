
# Program 4: Count Vowels in a String

# Take a string from the user
text = input("Enter a string: ")

# Convert the string into lowercase
text = text.lower()

# Initialize vowel counter
count = 0

# Check each character in the string
for ch in text:

    # Check whether the character is a vowel
    if ch in "aeiou":

        # Increase the count by 1
        count = count + 1

# Display the total number of vowels
print("Total number of vowels:", count)
