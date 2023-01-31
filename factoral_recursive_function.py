"""Problem:- Write a python program for factorial using user defined recursive function."""

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1)

num=int(input("Enter the number:-"))
print(f"Factorial of {num} is {fact(num)}")
