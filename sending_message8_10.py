# Modifying a list in a Functions

def show_messages(send_messages, sent_messages):
    while send_messages:
        current_message= send_messages.pop()
        print(f"Printing message: {current_message}")
        sent_messages.append(current_message)



def show_sentmessages (sent_messages):
    print("\nThe following messages have been sent :")
    for sent_message in sent_messages:
        print(f"{sent_message.title()} World!")

   

send_messages = ['hello', 'hi', 'bye']
sent_messages = []
show_messages(send_messages, sent_messages)
show_sentmessages(sent_messages)

# To check the status of orignal lists if messages are moved.
print(sent_messages)
print(send_messages)
