"""Problem:- Write a python program for Binary Search using recursive function."""

def binary(arr,ser):
    if ser in arr:
        no=len(arr)
        mid =no//2
        if(arr[mid]==ser):
            print(f"{ser} is in the array")
        elif(arr[mid]>ser):
            return binary(arr[0:mid],ser)
        elif(arr[mid]<ser):
            return binary(arr[mid:no],ser)

    else:
        print(f"{ser} is not in array")


arr=[]
no=int(input("Enter number of element:-"))
print("Enter the elements:-")
for i in range(no):
    ele=int(input())
    arr.append(ele)
ser=int(input("Enter the number you want to search:-"))
binary(arr,ser)