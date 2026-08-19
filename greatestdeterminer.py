# Program to find the greatest of four numbers

# Taking input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

# Using max() function (Pythonic way)
greatest = max(num1, num2, num3, num4)

print("\nThe greatest number is:", greatest)


# Manual comparison
"""greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4

print("The greatest number is:", greatest)"""
