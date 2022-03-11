fname=input("Please enter your first name:")
lname=input("please enter your last name:")
m=int(input('Please enter your Weighted Average marks:'))
if 100<=m<=70:
    classification="first class"
    message='Excellent,weldone!'
elif 60<=m:
    classification="upper class"
    message="Very good, well done!"
elif 50<=m:
    classification="Lower Second"
    message= "Good, well done!"
elif 40<=m:
    classification="third class"
    message= "could have done better!"
elif 35<=m:
    classification="Pass Degree"
    message= "Work harder next time!"
else:
    classification="fail"
    message='oh dear,try again!'

print(fname,lname, "You got", classification,message )