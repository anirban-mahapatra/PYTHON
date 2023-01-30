"""Problem:- Write a program to calculate GCD of two numbers using function"""

def fact(num,num1):
    min=0
    if(num>num1):
        min=num1
    else:
        min=num

    for i in range(min,0,-1):
        if(num%i==0 and num1%i==0):
            print(f"GCD of {num} and {num1} is {i}")
            break

num=int(input("Enter a number:-"))
num1=int(input("Enter another number:-"))
fact(num,num1)