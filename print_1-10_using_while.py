"""Problem:- Write a python program to print first 10 numbers using a while loop"""
i=0
while(i!=10):
    print(i+1,end="")
    i = i + 1
    if(i==10):
        print(end="")
    else:
        print(end=", ")
