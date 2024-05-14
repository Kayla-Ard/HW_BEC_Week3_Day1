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
# Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of Vehicle objects and updating their owners.

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
        
    def update_owner(self, owner):
        self.owner = owner
        print(f"The owner has been updated to {self.owner}")
    
vehicle1 = Vehicle('123456', 'Benz', 'Matt')
vehicle2 = Vehicle('456784', 'Chevy', 'Robert')
print(vehicle1.registration_number)
print(vehicle1.type)
print(vehicle1.owner)
print(vehicle2.registration_number)
print(vehicle2.type)
print(vehicle2.owner)
vehicle1.update_owner('Ricky')



# Task 2: Event Management System Enhancement
# Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants.
# Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.

class Event:
    def __init__(self, name, date, part):
        self.name = name
        self.date = date
        self.participants = part
        
    def add_participant(self):
        self.participants += 1
        print("One participant was added!")
    
    def get_participant_count(self):
        print(f"The current participant count is {self.participants}")
    
participants = Event(part = 50, name = "Susie", date = "Feb 10")
participants.add_participant()
participants.add_participant()
participants.get_participant_count()