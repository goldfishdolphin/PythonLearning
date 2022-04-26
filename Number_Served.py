# 9-1 Resturant
class Resturant:
    #A simple attempt to model a resturant.
    def __init__(self,resturant_name, cuisine_type):
        # Initialize resturant name and cuisine tyoe attributes.
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 10
        


    def describe_resturant(self):
        # Stimulate resturant's description according to name and cuisine type.
        print(f"\nThe name of the resturant is {self.resturant_name}.")
        print(f"This resturant serves {self.cuisine_type} food.")

    def open_resturant(self):
        #Stimulate that the resturant is open when command is called.
        print(f"The resturant {self.resturant_name} is open.")
    
    def number_serving(self):
        #Set the number of customers that have been served.
        print(f"The resturant{self.resturant_name} has served {self.number_served} people.")
'''
    def set_number_served(self,number_of_customers):
        """Set number of customers to given number"""
        self.number_served = number_of_customers
        '''

resturant = Resturant('Nawab', 'Desi')

resturant.describe_resturant()
resturant.number_served = 30
resturant.number_serving()