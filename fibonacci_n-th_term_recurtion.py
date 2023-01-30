"""Problem:- Write a program to find n-th Fibonacci numbers using user defined recursive function"""

def fibo(a,b,c,num):
    if(num==1):
        return c
    elif(num==2):
        return c
    else:
        c=a+b
        a=b
        b=c
        return fibo(a,b,c,num-1)

def fibo1(a,b):
    if (num==1):
        return a
    else:
        return b

num=int(input("Enter the number of term:-"))
if(num==1 or num==2):
    print(f"The {num} number terms is {fibo1(0,1)}")
else:
    print(f"The {num} number terms is {fibo(0,1,0,num)}")