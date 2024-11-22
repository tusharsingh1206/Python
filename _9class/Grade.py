grade=float(input())
if(grade>=90):
    print("Distinction")
elif(grade>=80 and grade<=89):
    print("First Class")
elif(grade>=70 and grade<=79):
    print("Second Class")
elif(grade>=60 and grade<=69):
    print("Pass")
else:
    print("Fail")