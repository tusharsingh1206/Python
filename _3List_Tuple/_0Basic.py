# A built-in data type that stores set of values.It can store elements of different
# types(int,float,string etc) some examples are student=["Ram",85,"Delhi"]
#It is like a array and we can fetch any data from index which start from 0.
#Strings are immutabe and the Lists are mutable in the python.
marks=[34,45,34,46,151.45,125.15,"Hello",'Tushar',"""Singh"""]
print(marks)
print(type(marks))
print(len(marks))
print(marks[3])
print(marks[7])
marks[4]=50
print(marks)