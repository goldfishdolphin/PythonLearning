#Positional argument
'''
def make_shirt(size,message):
    print(f"The size of the shirt is {size.tilte}")
    print(f"\nThe text to be printed is {message.title()}.")
make_shirt('large', 'hello world')
    '''
#Keyword argument
'''''
def make_shirt(size,message):
    print(f"The size of the shirt is {size.title()}")
    print(f"\nThe text to be printed is {message.title()}.")

make_shirt(size='large', message='hello world')
    '''
    
    # 8-4 Large shirt Default value

def make_shirt(message,size='large'):
    print(f"The size of the shirt is {size.title()}")
    print(f"\nThe text to be printed is {message}.")

make_shirt('I love Python')

