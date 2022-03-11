'''i=int(input("Please enter your income:£"));
if i>150000:
   rate=45
   band="additional"
elif i>=46351:
    rate=40
    band="Higher rate"
elif i>=11851:
    rate=20
    band="Basic rate"
else:
    rate=0
    band="Personal Allowance"


print( "Your band is " , band," and your tax rate is", rate,"%")
'''
i=int(input(" Please enter your income:"))
if i<=11850:
    rate=0
    band="personal allowance"
elif i<=46350:
    rate=20
    band="basic"
elif i<=150000:
    rate=40
    band="higher"
else:
    rate=45
    band="additional rate"

print(" Your band is", band, "and your tax rate is",rate )
