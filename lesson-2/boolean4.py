num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All numbers are different.")