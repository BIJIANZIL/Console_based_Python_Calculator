#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


# Welcome Message
def welcome():
    print('''
Welcome to Advanced Calculator
''')


# Define our functions for various mathematical operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y


def power(x, y):
    return x ** y


def square_root(x):
    return math.sqrt(x)


def modulus(x, y):
    return x % y


# List to store calculation history
calculation_history = []


# Display menu options
def display_menu():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. View Calculation History")
    print("9. Exit")


# Function to handle user input validation for choice
def get_choice():
    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")
        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return choice
        else:
            print("Invalid input. Please enter a valid choice.")


# Dictionary mapping choices to functions
operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide,
    '5': power,
    '6': square_root,
    '7': modulus
}


# Main loop for calculator functionality
def main():
    welcome()
    while True:
        display_menu()
        choice = get_choice()

        if choice == '9':
            print("Exiting Calculator. Goodbye!")
            break
        elif choice == '8':
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

        operation = operations[choice]
        if choice == '6':
            result = operation(num1)
        else:
            result = operation(num1, num2)

        print_result(result, choice)

        calculation_str = generate_calculation_str(result, choice, num1, num2)
        calculation_history.append(calculation_str)

        next_calculation = get_next_calculation()
        if next_calculation.lower() == "no":
            print("Exiting Calculator. Goodbye!")
            break


def print_result(result, choice):
    if choice == '6':
        print("Result: {:.2f}".format(result))
    else:
        print("Result:", result)


def generate_calculation_str(result, choice, num1, num2=None):
    if choice == '6':
        return f"sqrt({num1}) = {result:.2f}"
    else:
        return f"{num1} {'+-*/^sqrt%'[int(choice) - 1]} {num2} = {result}"


def get_next_calculation():
    while True:
        next_calculation = input("Let's do the next calculation? (yes/no): ")
        if next_calculation.lower() in ["yes", "no"]:
            return next_calculation
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()


# In[ ]:




