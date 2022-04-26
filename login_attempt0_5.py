
class User:
    '''A simple attempt to represent a user.'''
    def __init__(self, first_name, last_name, age, location):
        '''Initialize attributes to describe a user'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempt = 0



    def describe_user(self):
        '''Stimulate user description when command is called'''
        print(f"\nThe name of user is {self.first_name} {self.last_name}")
        print(f"The age of this user is {self.age} years.")
        print(f"The location of {self.first_name} {self.last_name} is {self.location}.")


    def greet_user(self):
        '''Stimulate greet user when this command is called.'''
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login(self,login):
        '''Increase the login attempt by given number'''
        self.login_attempt += login


    def reset_login_attempt(self):
        '''Reset the number of the login attempts'''
        self.login_attempt = 0

    def print_attempts(self):
        '''Print the number of attempts'''
        print(f'The current number of attempts is {self.login_attempt}.')

user = User('tim', 'yang', 10, 'Manchester')

user.describe_user()
user.greet_user()
user.print_attempts()
user.increment_login(20)
user.print_attempts()
user.reset_login_attempt()
user.print_attempts()
user.increment_login(10)
user.print_attempts()
user.reset_login_attempt()
user.print_attempts()