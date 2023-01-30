"""Problem:- Write a program to find whether the given number is an Amstrong number or not."""

num=int(input("Enter the number:-"))
i=0
n=num
temp=n
arm=0

while(temp>0):
    temp=temp//10
    i=i+1

for j in range(0,i):
    mo=n%10
    arm=arm+(mo**i)
    n=n//10

if(num==arm):
    print(num,"is a armstrong number")

else:
    print(num,"is not a armstrong number")