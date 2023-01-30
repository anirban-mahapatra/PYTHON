"""Problem:- Write a python program to count the number of elements in a List using user define recursive
 function."""

def cnt(list):
    if (list):
        return 1+cnt(list[1:])
    else:
        return 0

list=[1,2,3,4,5,6,7,8,9,10]
print(cnt(list))