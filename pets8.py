
#Positional argument
'''
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
'''
# Mutltiple Function Calls
'''
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','willie')'''

# Keyword arguments
'''
def describe_pet(animal_type, pet_name):
    # Display information about a pet.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='harry', animal_type='hamster')
'''

# Default Values
def describe_pet (pet_name, animal_type='dog'):
    # Display information about me.
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('Willie')
describe_pet(pet_name='harry', animal_type='hamster')
