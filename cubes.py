"""cubes=[]
for value in range(1,11):
    values=value**3
    cubes.append(values)

print(cubes)"""""

cubes=[value**3 for value in range(1,11)]
print('The first 3 items in the list are:')
print(cubes[:3])

print("Three items from the middle :")
print(cubes[3:6])
print(cubes)
print(cubes[7:])