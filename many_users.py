users= {
    'aiestein':{
        'first': 'albert',
        'last': 'aiestein',
        'location': 'princeton'
        },
    'murcie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFullname: {fullname.title()}")
    print(f"\tLocation: {location.title()}")