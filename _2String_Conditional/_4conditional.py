# #Syntax:if-elif-else
# """if(condition):
# statement1
# elif(condition)
# statement2
# else
# statement3
#  """
#  #In VScode tab means four spaces in python we start with a tab whwn we write the 
#  #statement in the next line and when we give this 4 spaces is called indentation 
#  #in the programming and in python no use of the curly braces
 
# age=int(input())
# if(age>20):
#      print("Applicable for marry")
#      print("can drive")
# elif(age<20):
#     print("can move")
# else:
#     print("can't move to anywhere")
        
#Nesting condition in the python is also applicable
age=int(input("Enter your age:"))
if(age>18):
    if(age>30):
        print("Adult")
    else:
        print("Less Adult")
else:
    print("Child")

 
 