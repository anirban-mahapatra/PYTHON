"""Problem:- Write a program to find all Fibonacci numbers after 100 but less than 1000."""

a=0
b=1
print("All fibonacci number between 100 to 1000:-",end=(" "))
while(1):
    c=a+b
    a=b
    b=c

    if(c>=1000):
        break
    elif(c>=100):
        print(c,"\t",end=(""))

