#Armstrong................
# n=int(input())
# digit=len(str(n))
# temp=n
# sum=0
# while temp>0:
#     r=temp%10
#     sum=sum+r**digit
#     temp//=10
# if sum==n:
#     print("Armstrong Number")
# else:
#     print("Not a Armstrong Number")

#palindrome.................
# n=int(input())
# temp=n
# sum=0
# while temp>0:
#     r=temp%10
#     sum=sum*10+r
#     temp//=10
# if sum==n:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

#Reverse the number
# n=int(input())
# sum=0
# while n>0:
#     r=n%10
#     sum=sum*10+r
#     n//=10
# print(sum)

#Prime......................
# n=int(input())
# a=0
# if n<2:
#     print("Not a Prime Number")
# else:
#     for i in range(2,n):
#         if(n%i==0):
#            a=1
#            break
#     if a==0:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")

#Sum of digits..................
# n=int(input())
# sum=0
# temp=n
# while temp>0:
#     r=temp%10
#     sum=sum+r
#     temp//=10
# print(sum)

#leap year............................
# year=int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400==0):
#     print("Leap Year")
# else:
#     print("NOt a Leap Year")

#Greatest of three......................
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if a>b:
#     if a>c:
#         print("a is the grreatest")
#     else:
#         print("c is the greatest")
# else:
#     if b>c:
#         print("b is the greatest")
#     else:
#         print("c is the greatest")

#swapping with and withou using third variable............
# a,b=10,20
# print(a,b,sep=",")
# a,b=b,a
# print(a,b,sep=",")
# temp=a
# a=b
# b=temp
# print(a,b,sep=",")

#Take five no as input and display largest and second largest........
# num1 = 10
# num2 = 20
# num3 = 5
# num4 = 30
# num5 = 15
# numbers = [num1, num2, num3, num4, num5]
# numbers.sort(reverse=True)
# largest = numbers[0]
# second_largest = numbers[1]
# print("Largest number:", largest)
# print("Second largest number:", second_largest)


#Convert the total seconda in the hours,minutes andd seconds
# total_second=int(input("Enter the total seconds"))
# hours=total_second//3600
# minutes=(total_second%3600)//60
# seconds=total_second%60
# print(f"{total_second} seconds is equivalent to {hours} hours, {minutes} minutes, and {seconds} seconds.")

#Print the ASCII code..........................
# a=input()
# for char in a:
#     print(ord(char))

#use of f in the python.........................
# name = "John"
# age = 30
# greeting = f"Hello, {name}. You are {age} years old."
# print(greeting) # Output: Hello, John. You are 30 years old

# price = 19.999214578
# quantity = 3
# total = f"Total: ${price + quantity:.4f}"
# print(total) # Output: Total: $59.97

#pattern.............................

# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *
# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print("* ",end=" ")
#     print(" ")

# *  *  *  *  *   
# *  *  *  *   
# *  *  *   
# *  *   
# *  
# n=int(input())
# for i in range(n,0,-1):
#     for j in range(i):
#         print("* ",end=" ")
#     print(" ")

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5 
# n=int(input("Enter the value of n:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# 1 2 3 4 5  
# 1 2 3 4  
# 1 2 3  
# 1 2  
# 1  
# n=int(input("Enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# n=int(input("Enter the value of n:"))
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print(" ")

# for num1 in range(3):
#     for num2 in range(10, 14):
#         print(num1, ",", num2)

# sum=0
# for i in range(1,21):
#     if (i%2!=0) and(i%3!=0) and(i%5!=0):
#         sum=sum+i
# print(sum)

# for i in range(10,0,-1):
#     print(i,end=" ")


# a='python programming'
# a[::-2]
# print(a)
# a[-17:14]
# print(a)

#Factoral of n using recursive
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# num=int(input())
# if num<0:
#     print("Not Possible")
# else:
#     print(f"The factorial of{num} is: {factorial(num)}")
# 


#Sum until single digit
# num = int(input("Enter a non-negative integer: "))
# if num < 0:
#     print("Please enter a non-negative integer.")
# else:
#     while num >= 10:  
#         total = 0  
#         temp = num  
#         while temp > 0:
#             digit = temp % 10  
#             total += digit      
#             temp //= 10        
#         num = total  
#     print(f"The sum of the digits until a single digit is: {num}")


# for i in range(5,10,-1):
#     print(i,"#")
# print('End')

j=5
for i in 'computer':
    j+=1
print(j)