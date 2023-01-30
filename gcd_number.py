"""Problem:- Write a program to calculate GCD of two numbers using for loop."""

num=int(input("Enter the first element:-"))
num1=int(input("Enter the second element:-"))
if(num>num1):
    n=num
    num=num1
    num1=n

if(num1%num==0):
    print("GCD of",num,"and",num1,"is",num)
else:
    p=num-1
    for i in range (p,0,-1):
        if(num%i==0 and num1%i==0):
            print("GCD of",num,"and",num1,"is",i)
            break