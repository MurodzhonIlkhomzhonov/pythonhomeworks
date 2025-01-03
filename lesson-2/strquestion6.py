# Task 6: Check if one string contains another

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if string2 in string1:
    print(f"'{string2}' is present in '{string1}'.")
else:
    print(f"'{string2}' is not present in '{string1}'.")