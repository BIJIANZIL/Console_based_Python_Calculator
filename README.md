# Simple Python Calculator

A basic command-line calculator implemented in Python.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- User-friendly command-line interface.
- Handles division by zero gracefully.

## Usage

To use the calculator, follow these steps:

1. Enter the desired operation:(Select Desired operation)
   - Type `1 for addition
   - Type `2` for subtraction
   - Type `3` for multiplication
   - Type `4` for division
   - Type `quit` to end the program

2. Follow the prompts to enter the necessary values.

### Examples

```plaintext

>> Enter operation: 1
>> Enter first number: 5
>> Enter second number: 3
>> Result: 8

>> Enter operation: 4
>> Enter first number: 10
>> Enter second number: 0
>> Error: Cannot divide by zero. Please enter a valid divisor.

>> Enter operation: quit
>> Program terminated.

``````
# 2.UML

# 1.Use Case Diagram

![Image](usecasediagram.png)

# 2.[**Activity Diagram:**](https://github.com/BIJIANZIL/Console_based_Python_Calculator/blob/main/activitydiagram.png)

![Image1](activitydiagram.png)

# 3.Sequence Diagram

![Image2](sequencediagram.png)

# 3.DDD

![Image](domaindiagram.png)

# 4.METRICS

SonarQube is a code review tool that systematically helps us deliver Clean Code.It checks for bugs and vulnerabilities in the project and provide recommendations to resolve the code smells.
Below are the snippets of metrics:

![Image](Sonarqube1.png)

![Image](SonarQube2.png)

# 5.Clean Code Development

# 1.Modular Design
In the calculator code,functions like add,subtract etc handle specific arithmetic operation.This aligns with the Single responsibility Principle(SRP),making the code modular and easy to maintain.Each function can be modified independently without affecting others.

# 2.Proper input validation and Error Handling
The code includes input validation for numerical entries and handles potential errors, such as division by zero.This practice enhances user experience by providing clear feedback and prevents unexpected crashes.

# 3.Descriptive names for variables and functions.
Variable names like num1 ,num2 and functions like add,subtract are clear and convey their purpose.This improves the code's self-documenting nature,reducing the need for excessive comments.
Developers can easily understand the role of variables and functions without deep analysis.

# 4.User-Friendly Interface.
The program provides clear prompts and messages to guide the user through each step of the calculation process.It also offers the option to view calculation history enhancing the overall user experience.

# 5.Comments
Although the code is self-explanatory,few comments have been added to help someone understand the easiest way possible.

# 6.Build Management
To understand build management, I have selected Gradle build automation tool that supports multiple languages . It controls the development process in the tasks of compilation and packaging to testing,deployment and publishing.I set up a simple project in IntelliJ IDEA IDE running "Hello, World!" program in Java and used Groovy DSL (scripting build configurations ) and  generated documentation, and run the tests.

First I have created a new Gradle Project with Java as language and created Java class and wrote main.java program to print "Hello, World!".And wrote test class -MainTest to check if it is functioning properly.Understanding build.gradle-here is where is we define our project's configuration, dependencies, and tasks. IntelliJ IDEA provides excellent support for Gradle projects. Gradle provides tasks for running tests, such as the test task. We can execute this task to run all the tests in our project.<br/>
![gradlebuild](https://github.com/BIJIANZIL/Console_based_Python_Calculator/blob/main/gradlebuild.png)
![Main](https://github.com/BIJIANZIL/Console_based_Python_Calculator/blob/main/Main.png)
![Test](https://github.com/BIJIANZIL/Console_based_Python_Calculator/blob/main/Test.png)

<br/>Reference:[https://github.com/BIJIANZIL/Console_based_Python_Calculator/gradle-demo](https://github.com/BIJIANZIL/gradledemo.git) <br/>




# 7.Continous Delivery



# 8.Unit Tests
Unit test was also performed using Gradle on the same Java program.<br/>
![Test](https://github.com/BIJIANZIL/Console_based_Python_Calculator/blob/main/Test.png)


# 9.IDE




# 10.DSL


# 11.Functional Programming





