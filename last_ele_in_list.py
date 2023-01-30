"""Problem:-Write a python program to find the last element of a List using user define recursive function."""

def coun(list):
    if(list):
        return 1+coun(list[1:])
    else:
        return 0

list=[10,20,30,40,50,60,70,80,90]
cnt=coun(list)
print("The last element of the list is ",list[cnt-1])