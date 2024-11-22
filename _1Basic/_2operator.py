#Arithmetic Operators(+,-,*,/,%,**)
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)#it is used to find the remainder
print(a**b)#it is used to find the power a to the power b
#Relational/Comparison Operators(==,!=,>,<,>=,<=)
#This operator will always give True or False value
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#Assignment Operators(=,+=,-=,*=,/=,%=,**=)
a**=2 #a to the power 2
print(a)
#Logical Operators(not,and ,or)
print(not True)
print(not False)
print(not(a>b))

val1=True
val2=False
print("and operator is:",val1 and val2)
print("and operator is:",(a==b) and (a>b))#both must be true
print("or operator is:",val1 or val2)
print("or operator is:",(a==b) or (a>b))