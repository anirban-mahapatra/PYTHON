"""Problem:- Write a Python program to compute the reverse of a number using function."""

def rev(n):
    r=0
    while(n!=0):
        m=n%10
        n=n//10
        r=r*10+m
    return r

num=int(input("Enter the number:-"))
print(num,"revers number is",rev(num))