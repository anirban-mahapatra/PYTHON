"""Problem:- Write a program to calculate GCD of two numbers using user defined recursive function"""

def gcd(num,num1,min):
    if(num%min==0 and num1%min==0):
        return min
    else:
        return gcd(num,num1,min-1)
def mini(num,num1):
    min = 0
    if(num>num1):
        min=num1
        return min
    else:
        min=num
        return min

num=int(input("Enter first number:-"))
num1=int(input("Enter second number:-"))
mini(num,num1)
min1=mini(num,num1)
print(f"The GCD of {num} and {num1} is {gcd(num,num1,min1)}")