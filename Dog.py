# Creating and using a class

class Dog:
    '''A simple attempt to model a dog.'''
    def __init__(self, name, age):
        '''Initialize name and age attributes.'''
        self.name = name
        self.age = age

    def sit(self):
        '''Stimulate a dog sitting in response to a command.'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Stimulate a dog rolling over in response to a command.'''
        print(f"{self.name} rolled over!")


#Making an instance from a Class
my_dog=Dog("Willie",6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Calling Methods
my_dog.sit()
my_dog.roll_over()

#Creating Multiple instances
your_dog=Dog('Lucy', 3)

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()
