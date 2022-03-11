transport=[]

transport.append('ducati')
transport.append('honda')
transport.append('suzuki')
transport.insert(0,'yamaha')
print(transport)
last_owned=transport.pop()
print(f"The last mototorcycle I owned was {last_owned.title()}.")
first_own=transport.pop(0)
print(f"The first motorcycle I owned was {first_own.title()}. ")