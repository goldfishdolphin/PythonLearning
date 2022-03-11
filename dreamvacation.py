
places = {}
polling_active = True
while polling_active:

# prompt users to enter their name
    name = input('Please enter your name:')

# prompt users to enter their response

    place = input ('What is your dream vaccation place?')
    places[name] = place
    # Find if anyone else is going to take the poll.
    repeat = input("Would you like to let anyone else respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n --Poll Results-- ")

for name, place in places.items():
    print(f"{name.title()} would like to visit {place.title()}")

