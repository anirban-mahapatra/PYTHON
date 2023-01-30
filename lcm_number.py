"""Problem:- Write a program to compute LCM of any number."""

num=int(input("Enter the first number:-"))
number=int(input("Enter the second number:-"))

max=num if(num>number) else number

while(True):
    if(max%num==0 and max%number==0):
        lcm=max
        break
    max+=1
print("LCM of",num,"and",number,"is",lcm)