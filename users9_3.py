
class User:
    '''A simple attempt to represent a user.'''
    def __init__(self, first_name, last_name, age, location):
        '''Initialize attributes to describe a user'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location


    def describe_user(self):
        '''Stimulate user description when command is called'''
        print(f"\nThe name of user is {self.first_name} {self.last_name}")
        print(f"The age of this user is {self.age} years.")
        print(f"The location of {self.first_name} {self.last_name} is {self.location}.")


    def greet_user(self):
        '''Stimulate greet user when this command is called.'''
        print(f"Hello {self.first_name} {self.last_name}!")


user1 = User('tim', 'yang', 10, 'Manchester')
user2 = User('jimmiy', 'mickie', 15, 'Pakistan')
user3 = User('Jim', 'Kim', 70, 'Manchester')
user4 = User('Micky', 'Madrigal', 18, 'Columbia')
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()