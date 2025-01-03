# Task 5: Count vowels and consonants

vowels = "aeiouAEIOU"
string_to_check = input("Enter a string: ")
vowel_count = sum(1 for char in string_to_check if char in vowels)
consonant_count = len(string_to_check) - vowel_count
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")