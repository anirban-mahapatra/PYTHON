"""Problem:- Write a python program for Insertion sort using function."""

# def sort(arr,no):
#     for i in range(1,no):
#         key=arr[i]
#         j=i-1
#         while(j>=0 and arr[j]>key):
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key


def sort(arr,no):
    for i in range(1,no):
        j=i-1
        while(j>=0 and arr[j]>arr[j+1]):
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j-=1

arr=[]
no=int(input("Enter number of element:-"))
print("Enter the elements:-")
for i in range(no):
    ele=int(input())
    arr.append(ele)
sort(arr,no)
print(arr)

