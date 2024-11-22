# a=int(input())
# if(a==1):
#     print("Monday")
# elif(a==2):
#     print("Tuesday")
# elif(a==3):
#     print("Wednesday")
# elif(a==4):
#     print("Thursday")
# elif(a==5):
#     print("Friday")
# elif(a==6):
#     print("Saturday")
# elif(a==7):
#     print("Sunday") 
# else:
#     print("No day of the week")

a=int(input())
match a:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day number. Please enter a number between 1 and 7.")
        