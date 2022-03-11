
responses={}
polling_active = True

while polling_active:
    name = input('\nPlease enter your name:')
    response = input('Which mountain would you like to climb someday?')
    responses[name]=response
    repeat=input('Would you like to let another person respond? (yes/no)')
    if repeat == 'no':
        polling_active = False


print("--Poll Results ---")
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
'''
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the peron's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
'''