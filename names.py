friends=['Eshaal','Rayyan','Aysha']
#'Hoorain','Faaiz','Rafay','Maaz
friend_missing=friends.pop(1)
print(f"The friend who is not attending the party is {friend_missing} ")
friends.append(('HOORAIN').title())

friends.insert(0,'Faaiz')

friends.insert(2,'Rafay')

friends.append('Maaz')

popped_person=friends.pop()
print(f"Sorry {popped_person} I can not invite you as table is not being delivered on time. ")
popped_person=friends.pop()
print(f"Sorry {popped_person} I can not invite you as table is not being delivered on time. ")
popped_person=friends.pop()
print(f"Sorry {popped_person} I can not invite you as table is not being delivered on time. ")
popped_person=friends.pop()
print(f"Sorry {popped_person} I can not invite you as table is not being delivered on time. ")
print("Hi" ,friends[0],"! I am looking forward to meet you.")
print("Hi" ,friends[1],"! I am looking forward to meet you.")
del friends[1]
del friends[0]
print(friends)
