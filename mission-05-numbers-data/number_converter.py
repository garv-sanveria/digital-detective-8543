# Number converter program for Mission 5

# Ask the user to enter a decimal number
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary and hexadecimal
binary_number = bin(decimal_number)
hex_number = hex(decimal_number)

# Display the results
print("Binary:", binary_number)
print("Hexadecimal:", hex_number)
