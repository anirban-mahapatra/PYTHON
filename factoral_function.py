"""Problem:- Write a Python program to compute the factorial of given integer using function"""

def fac(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of %d is %d"%(num,fact))

num=int(input("Enter the number:-"))
fac(num)