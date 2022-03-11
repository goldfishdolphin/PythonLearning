from email import message


topping = "\nPlease enter your desired toppings:"
topping += "\nPlease enter 'quit' when you are done."

'''message = ""

while message != 'quit':

    message =input(topping)

    print(f'We ll add {message} to your pizza.')'''

'''
while True:
    message = input(topping)

    if message == 'quit':
        break
    else:
        print(f'We ll add {message} to your pizza.')'''

active = True
while active:
    message=input(topping)

    if message == 'quit':
        active = False
    else:
        print(f'We ll add {message} to your pizza.')