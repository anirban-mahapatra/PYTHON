"""Problem: Write a python program to find the following sum using user defined recursive function.
                    S=1+2+3+ ... ... .... +19+20."""

def sum(num,s):
    if(num<=20):
        s=s+num
        return sum(num+1,s)
    else:
        return s

print("Sum=",sum(1,0))