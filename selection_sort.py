"""Problem:- Write a python program for Selection sort using function."""

def selection(arr,no):
    for i in range(no):
        min=arr[i]
        for j in range(i+1,no):
            if(min>arr[j]):
                min=arr[j]
        (arr[i],min)=(min,arr[i])
    print(arr)

arr=[]
no=int(input("Enter the number of element:-"))
for i in range(no):
    ele=int(input("Enter the elements:-"))
    arr.append(ele)
