#Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are going to make."""
    print("\n Making a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza(16,'peperoni')
make_pizza(12, 'mushroom', 'onion', 'extra cheese', 'green peppers')
