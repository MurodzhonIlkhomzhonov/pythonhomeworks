# Task 11: Check if string contains digits

string_input = input("Enter a string: ")
if any(char.isdigit() for char in string_input):
    print("The string contains digits.")
else:
    print("The string does not contain digits.")