# Task 1: Ask name and year of birth, then calculate age

name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
current_year = 2024
age = current_year - year_of_birth
print(f"Hello {name}, you are {age} years old.")