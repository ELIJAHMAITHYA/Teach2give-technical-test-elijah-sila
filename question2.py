# Write a recursive function to calculate the factorial of a number
from math import factorial


def calculate_Factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

    # Example


print(calculate_Factorial(45))
print(calculate_Factorial(0))
print(calculate_Factorial(5))
