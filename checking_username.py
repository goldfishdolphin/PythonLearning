current_users = ['admin','JIN','Naomi','john','jamie','john']
new_users = ['jamie','tim','Admin','mina','tina','John']
current_users =[x.lower() for x in current_users]
new_users = [x.lower() for x in new_users]

for new_user in new_users:
    if new_user in current_users:
        print(f'{new_user} already exist. Please try another username.')
    else:
        print(f'username {new_user} is available. ')