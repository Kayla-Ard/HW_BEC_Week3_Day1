# Python Modules and Data Handling Assignment - TASK 1: YOUR MOOD TODAY
from mood import moods
mood_response = moods()
if mood_response == "happy":
    print("It's awesome that you are happy today! YAY!")
elif mood_response == "sad":
    print("Sorry you are sad today, hope that changes soon for you!")
elif mood_response == "excited":
    print("It's awesome that you are excited today! YAY!")
else:
    print("Invalid response")
    


# Mastering Python Modules and Aliases - TASK 1: CUSTOM MODULE WITH ALIASES 
import text_utils as tu
str = input("Tell me about your day please: ")
print(tu.reverse_string(str))
print(tu.capitalize_string(str))
