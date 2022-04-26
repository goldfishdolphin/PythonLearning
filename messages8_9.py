# Passing a list to a function.
def show_messages(messages):

    for message in messages:
        msg = f"{message.title()} World! "
        print(msg)

short_messages=['hello', 'hi', 'bye']
show_messages(short_messages)