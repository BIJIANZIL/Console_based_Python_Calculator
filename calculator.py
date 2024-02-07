#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

# Welcome Message
def welcome():
    print('''
Welcome to Advanced Calculator
''')

welcome()

# Define our function

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# This function calculates the power of a number
def power(x, y):
    return x ** y

# This function calculates the square root of a number
def square_root(x):
    return math.sqrt(x)

# This function calculates the modulus of two numbers
def modulus(x, y):
    return x % y

# List to store calculation history
calculation_history = []

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square Root")
print("7.Modulus")
print("8.View Calculation History")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    # check if choice is one of the options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '8':
            # View Calculation History
            if not calculation_history:
                print("No calculations in history.")
            else:
                print("Calculation History:")
                for calculation in calculation_history:
                    print(calculation)
                print()
            continue

        try:
            num1 = float(input("Enter first number: "))
            if choice != '6':
                num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = power(num1, num2)
        elif choice == '6':
            result = square_root(num1)
        elif choice == '7':
            result = modulus(num1, num2)

        # Print the result
        print("Result:", result)

        # Save the calculation to history
        if choice == '6':
            calculation_str = f"sqrt({num1}) = {result}"
        else:
            calculation_str = f"{num1} {['+', '-', '*', '/', '**', 'sqrt', '%'][int(choice) - 1]} {num2} = {result}"

        calculation_history.append(calculation_str)

        # check if the user wants another calculation
        while True:
            next_calculation = input("Let's do the next calculation? (yes/no): ")
            if next_calculation.lower() in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid Input")


# In[ ]:




