"""Problem:- Write a Python program to print star pattern and reverse star pattern"""

num=int(input("Enter number of rows:-"))
b=int(input("Enter 0 to print Star Pattern and 1 for Revers Star Pattern:-"))
if b==0:
    for i in range (0,num):
        for j in range (0,i+1):
            print("*",end=' ')
        print()
elif b==1:
    for i in range(0,num):
       for j in range (num,i,-1):
            print("*",end=' ')
       print()
else:
    print("You enter wrong input")