prompt = "\nPlease enter your age:"
prompt+= "\n(Please enter 'quit' when you are done)"

active = True
while active:
    age=input(prompt)

    if age == 'quit':
        break

    age= int(age)

    if age < 3:
        print('price=0')

    elif age <= 12:
        print('price=10')
    
    else:
        print('price=15')




'''

3 <= age <= 12 :
    price=10

print("fThe price to be paid for your ticket: $ {price}")
if age < 3:
    price=0
else: 
    price=15


print("fThe price to be paid for your ticket: $ {price}")'''