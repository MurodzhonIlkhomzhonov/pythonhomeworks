# Task 18: Check if a string starts and ends with specific words

string_input = input("Enter a sentence: ")
start_word = input("Enter the start word: ")
end_word = input("Enter the end word: ")
if string_input.startswith(start_word) and string_input.endswith(end_word):
    print("The string meets the conditions.")
else:
    print("The string does not meet the conditions.")