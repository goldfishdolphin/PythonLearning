user=input("Please enter the user status , (student or staff)")
p=float(input("please enter the price of an item:"))
if user=="student":
    p=p*.9
elif user=="staff":
    p=p

else:
    user="unknown"
    p=p
    print("Do not qualify for discount. Please pay £:", p)


print("the bill:£",p)