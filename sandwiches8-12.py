def make_sandwich(*items):
    "Print the summary of the sandwich that is being ordered."
    print("\nMaking the sandwich with the following items:")
    for item in items:
        print(f"- {item.title()}")

make_sandwich('cheese', 'tomato')
make_sandwich('butter', 'peper', 'chicken')
make_sandwich('egg', 'mayo')