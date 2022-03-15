# Simple Value
'''def get_formatted_name(first_name, last_name):
    # Return neatly formatted full name.
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician=get_formatted_name('woody', 'kim')
print(musician)'''

# Making Argument Optional
def get_formatted_name(first_name, last_name,middle_name=''):
    # Return neatly formatted full name.
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"

    return full_name.title()

musician=get_formatted_name('woody', 'kim', 'tina')
print(musician)