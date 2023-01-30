"""Problem:- Write a python program to find the sum of integer elements of a List using user defined
recursive function."""

def count(list,n,sum):
    while(list):
        sum=sum+list[n]
        return count(list[n+1:],n,sum)
    print("The sum of the list is",sum)

num=int(input("Enter the number of element:-"))
list=[]
print("Enter the elements:-")
for i in range(0,num):
    ele=int(input())
    list.append(ele)
count(list,0,0)
