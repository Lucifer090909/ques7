# Function to analyze a string and count various elements
def analyze_string(input_string):
    num_alphabets = num_digits = num_symbols = num_uppercase = num_lowercase = 0

    for char in input_string:
        if char.isalpha():
            num_alphabets += 1
            if char.isupper():
                num_uppercase += 1
            elif char.islower():
                num_lowercase += 1
        elif char.isdigit():
            num_digits += 1
        else:
            num_symbols += 1

    return num_alphabets, num_digits, num_symbols, num_uppercase, num_lowercase

# Input a string from the user
input_string = input("Enter a string: ")

# Call the analyze_string function to get information about the string
result = analyze_string(input_string)

# Unpack the result tuple
num_alphabets, num_digits, num_symbols, num_uppercase, num_lowercase = result

# Display the information
print("Number of alphabets:", num_alphabets)
print("Number of digits:", num_digits)
print("Number of symbols:", num_symbols)
print("Number of uppercase alphabets:", num_uppercase)
print("Number of lowercase alphabets:", num_lowercase)
