"""Problem:- Write a python function to find the sum of two numbers and return the result."""

def sum(num,num1):
    return num+num1

num=int(input("Enter the 1st number:-"))
num1=int(input("Enter the 2nd number:-"))
print(f"Sum of {num} and {num1} is {sum(num,num1)}")