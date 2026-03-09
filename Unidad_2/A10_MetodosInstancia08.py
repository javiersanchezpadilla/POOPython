""" In the code editor, you'll see that there's a Flight class already defined. 
    This class has an add_passenger() method.

    Step 1: Create an instance of this class and assign it to a variable named 
            flight. The flight number should be "NJ09".
    Step 2: Call the add_passenger() method on this instance to add the passenger 
            "Nora" (a string).
    Step 3: Call the add_passenger() method again on the same instance to add the 
            passenger "Gino" (a string)."""

class Flight:
    
    max_passengers = 3
    
    def __init__(self, number):
        self.number = number
        self.passengers = []
        self.waiting_list = []

    def add_passenger(self, passenger):
        if len(self.passengers) >= Flight.max_passengers:
            self.waiting_list.append(passenger)
        else:
            self.passengers.append(passenger)
        
# Write your code below:
flight = Flight('NJ09')
flight.add_passenger('Nora')
flight.add_passenger('Gino')
