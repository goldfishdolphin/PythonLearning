# 9-1 Resturant
class Resturant:
    #A simple attempt to model a resturant.
    def __init__(self,resturant_name, cuisine_type):
        # Initialize resturant name and cuisine tyoe attributes.
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type


    def describe_resturant(self):
        # Stimulate resturant's description according to name and cuisine type.
        print(f"\nThe name of the resturant is {self.resturant_name}.")
        print(f"This resturant serves {self.cuisine_type} food.")

    def open_resturant(self):
        #Stimulate that the resturant is open when command is called.
        print(f"The resturant {self.resturant_name} is open.")


# 9-2 Three Resturants (Different instances )

resturant1 = Resturant('Nawab', 'Desi')
resturant2 = Resturant('akbars', 'Indian')
resturant3 = Resturant('Wok', 'Thai')

resturant1.describe_resturant()
resturant2.describe_resturant()
resturant3.describe_resturant()





