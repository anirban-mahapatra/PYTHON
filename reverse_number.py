"""Problem:- Write a Python program to compute the reverse of a number using while loop"""

num=int(input("Enter the number:-"))
a=num
r=0
while(a!=0):
    rev=a%10
    a=a//10
    r=r*10+rev
print(num," reverse number is",r)