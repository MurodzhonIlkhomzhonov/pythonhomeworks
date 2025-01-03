# Task 12: Join list of words

words = input("Enter a list of words separated by spaces: ").split()
separator = input("Enter a separator: ")
joined_string = separator.join(words)
print(f"Joined string: {joined_string}")