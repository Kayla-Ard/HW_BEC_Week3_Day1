# Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.
# 2. Mastering Python Modules and Aliases
# Task 1: Custom Module with Aliases
# Problem Statement: Create a custom module named text_utils.py with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.
# Code Example:
# ```python
# # text_utils.py
# def reverse_string(s):
# # function to reverse a string
# def capitalize_string(s):
# function to capitalize a string
# main.py
# Import text_utils using an alias and utilize its functions
# Expected Outcome: Your main script should be able to use the functions from text_utils.py via an alias, demonstrating an understanding of custom module creation and aliasing.

def reverse_string(str):
    return str[::-1]

def capitalize_string(str):
    return str.upper()

