"""Problem:- Write a Python program to compute the factorial of given integer"""

n=int(input("Enter the number:-"))
fac=1
for i in range (1,n+1):
    fac=fac*i
print("The factorial of ",n,"is",fac)