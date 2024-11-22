#Tuple:A built in data type that lets us create immutale sequences of variables
a=(23,34,45,67,45,35)
print(type(a))
print(a[2])
#Empty tuple
b=()
#While creating tuple with only one element always write , after value other wise it will 
#consider it as the int,float or string type data and ignore the brackets
c=(1)
d=(2.0)
e=("Hello")
f=(1,)
print(type(c))
print(type(d))
print(type(e))
print(type(f))