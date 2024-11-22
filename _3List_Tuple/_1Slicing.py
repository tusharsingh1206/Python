#Slicing:Accessing parts of the string is called slicing
mark=[56,45,48,79,50]
print(mark[2:5])#It means from 2 to 4 index do not include last index
print(mark[:3])#It means from 0 to 2 index
print(mark[0:])#It means from 0 to last index
print(mark[0:len(mark)])#It means from 0 to last index
print(mark[6:len(mark)])#It only print braces

#negative index in the python is possible
#the last character have -1 index and then increase in the negatice value from right to left
#[56,45,48,79,50]-->-5(56) -4(45) -3(48) -2(79) -1(50)
print(mark[-3:-1])
print(mark[:-1])
print(mark[-1:-3])#does not print anything
print(mark[-5:])
