pizzas=['mexican','pepperoni','tikka']
'''for pizza in pizzas:
    print(f"I like {pizza.title()} pizza.")
    print(f"{pizza.title()} is so yummy!")
    print(f"Today I'll eat {pizza.title()} pizza. ")

print("I really love pizza!")'''
friends_pizzas=pizzas[:]
friends_pizzas.append('pineapple')
pizzas.append('fajita')

print('My favorit pizza are:')
for pizza in pizzas:
    print(pizza)

print('My friends favorit pizza are:')
for friendspizza in friends_pizzas:
    print(friendspizza)
