"""Problem:- Write a python program for Bubble sort using function."""

def sort(arr,no):
    for i in range(no-1):
        for j in range(no-i-1):
            if (arr[j]>arr[j+1]):
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
    return arr

arr=[]
no=int(input("Enter the number of elements:-"))
print("Enter the elements:-")
for i in range(no):
    ele=int(input(""))
    arr.append(ele)
print("The result in ascending order",sort(arr,no))