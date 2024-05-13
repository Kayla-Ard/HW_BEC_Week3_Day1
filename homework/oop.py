# City Infrastructure Management System
# Task 1: Vehicle Registration System
# Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner.
# Implement a method update_owner to change the vehicle's owner.
# Then, create a few instances of Vehicle and demonstrate changing the owner.
# Code Example: Provide a basic structure for the Vehicle class without methods.
# ```python
# class Vehicle:
# def init(self, reg_num, type, owner):
# self.registration_number = reg_num
# self.type = type
# self.owner = owner
# ```
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_number, type, owner):
        self.registration_number = reg_number
        self.type = type
        self.owner = owner
        
    def update_owner(self, owner):
        self.owner = owner
        print(f"The owner has been updated to {self.owner}")
    
vehicle1 = Vehicle(123456, 'Benz', 'Matt')  
print(vehicle1)  


# Task 2: Event Management System Enhancement

# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
# ```python
# class Event:
# def init(self, name, date):
# self.name = name
# self.date = date
# ```