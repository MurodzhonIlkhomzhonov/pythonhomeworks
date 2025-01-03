# Task 4: Check for palindrome

palindrome_input = input("Enter a string: ")
if palindrome_input == palindrome_input[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")