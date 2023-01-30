"""Problem:- Write a program to enter a number and then calculate the sum of its digits"""

num=int(input("Enter the number:-"))
n=num
sum=0
while(num>0):
    no=num%10
    sum=sum+no
    num=num//10
print(f"The total sum of {n} is {sum}")