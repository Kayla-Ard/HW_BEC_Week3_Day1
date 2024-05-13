# create a class for a bus
# an attribute for seats
# methods to pick up and drop off passengers to change the number of seats available
# if you're feeling SAUCY change the bus driver
# if you're feeling EXTRA SAUCY change the color of the bus

class Bus:
    def __init__(self, seats, driver, color):
        self.seats = seats 
        self.driver = driver 
        self.color = color
        
    def passenger_exit(self):
        self.seats -= 1
        print(f"Passenger exited the bus. Seats remaining: {self.seats}")
    
    def passenger_enter(self):
        self.seats += 1
        print(f"Passenger got on the bus. Seats remaining: {self.seats}")
    
    def bus_driver(self, driver):
        self.driver = driver
        print(f"Bus driver changed to {self.driver}")
    
    def bus_color(self, color):
        self.color = color
        print(f"Bus color changed to {self.color}")
    
my_bus = Bus(20, 'David', 'Blue')
my_bus.passenger_exit()
my_bus.passenger_exit()
my_bus.passenger_exit()
my_bus.passenger_enter()
my_bus.passenger_enter()
my_bus.bus_driver("George")
my_bus.bus_color("Purple")


