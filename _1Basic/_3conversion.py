#type conxersion which is automatic conversion done by the interpreter
a=2
b=4.35
sum=a+b #2.0+4.35=6.35
print (sum)
c="2"
#print(b+c)#it gives error because addition of the string and the integer is not allowed
#so we need to typecast it
d=int(c)
print(type(d))
print(a+d)
#type casting of the float in the string
a=43.455
a=str(a)
print(type(a))