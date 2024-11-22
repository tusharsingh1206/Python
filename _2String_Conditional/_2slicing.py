#Slicing:Accessing parts of the string is called slicing
s1="Hello my name is Tushar Singh"
print(s1[2:18])#It means it print from 2 to 17 index and do not include last index(18)
print(s1[:17])#It means from 0 to 17 index
print(s1[6:])#It means from 6 to last index
print(s1[6:len(s1)])#It means from 6 to last index

#negative index in the python is possible
#the last character have -1 index and then increase in the negatice value from right to left
#Apple-->-5(A) -4(p) -3(p) -2(l) -1(e)
s2="Apple"
print(s2[-3:-1])
print(s2[:-1])
print(s2[-1:-3])
print(s2[-5:])

s3="TUSHARSINGH"
print(s3[2:7])
