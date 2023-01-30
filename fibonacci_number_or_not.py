"""Problem:- Write a program to test whether a given number is Fibonacci number or not."""

def fibo(num):
    a=0
    b=1
    if(num==0):
       print(f"{num} is fibonacci number")
    elif(num==1):
        print(f"{num} is fibonacci number")
    else:
        while(1):
            c=a+b
            a=b
            b=c
            if(c==num):
                print(f"{num} is fibonacci number")
                break
            elif(c>num):
                print(f"{num} is not fibonacci number")
                break
num=int(input("Enter the number:-"))
fibo(num)