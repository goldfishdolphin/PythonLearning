class Car:
    '''A simple attempt to represent a car.'''
    def __init__(self,make, model, year):
        '''Initialize the attributes to describe a car.'''
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statment showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        """Set ododmeter reading to a given value.
        Reject the change if it attempts to roll the odometer back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odometer.")

    def increment_odometer (self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    '''A simple attempt to model a battery of an electric car.'''


    def __init__(self,battery_size=75):
        '''Intialize the attributes of a battery.'''
        self.battery_size = battery_size

    def describle_battery(self):
        '''Print a statement describing the battery size.'''
        print(f"This car has a  {self.battery_size}-kWh battery.")




class ElectricCar(Car):
    '''Represent aspect of a car, specific to electric vehicles.'''
    def __init__(self, make, model, year):
        ''''Intialize attributes of the parent class.
        Then intialize attributes specific to an electric car.'''
        super().__init__(make, model, year)
        self.battery = Battery()

    
my_tesla =ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describle_battery()