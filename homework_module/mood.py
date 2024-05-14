# Lesson 1 Assignments | Modules
# 1. Python Modules and Data Handling Assignment
# Task 1: Your Mood Today
# Problem Statement: Create a Python program using a custom module that asks the user how they are feeling today
# and responds with a custom message based on the mood entered.
# Code Example:
# ```python
# # mood_responses.py
# def mood_response(mood):
# # Implement your response logic here
# # main.py
# import mood_responses
# mood = input("How are you feeling today? ")
# print(mood_responses.mood_response(mood))

def moods():
    mood_response = input('What is your mood today? Please enter one of these responses: "happy", "sad" or "excited:" ').lower()
    return mood_response
