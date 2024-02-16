#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Side effect free function to calculate square of a number
def square(x):
    return x ** 2

# Higher order function to apply a function to each element of a list
def apply_function_to_list(func, lst):
    return [func(x) for x in lst]

# Function as parameter and return value to create a custom multiplier
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

# Closures to create specific multipliers
multiply_by_2 = create_multiplier(2)
multiply_by_5 = create_multiplier(5)
multiply_by_10 = create_multiplier(10)

# Using higher order function to apply custom multipliers to a list
def apply_multiplier_to_list(multiplier_func, lst):
    return [multiplier_func(x) for x in lst]

# Define some numbers
numbers = [1, 2, 3, 4, 5]

# Apply square function to each element of the list
squared_numbers = apply_function_to_list(square, numbers)
print("Squared numbers:", squared_numbers)

# Apply custom multipliers to each element of the list
custom_multiplied_by_2 = apply_multiplier_to_list(multiply_by_2, numbers)
print("Numbers multiplied by 2:", custom_multiplied_by_2)

custom_multiplied_by_5 = apply_multiplier_to_list(multiply_by_5, numbers)
print("Numbers multiplied by 5:", custom_multiplied_by_5)

custom_multiplied_by_10 = apply_multiplier_to_list(multiply_by_10, numbers)
print("Numbers multiplied by 10:", custom_multiplied_by_10)


# In[ ]:




