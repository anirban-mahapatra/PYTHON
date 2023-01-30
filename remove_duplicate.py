"""Problem:- Write a Python program to remove duplicate"""
ele=[]
uniq=[]
dupli=[]
a=int(input("Enter the number of elements:-"))
for i in range(0,a):
    x=int(input(f"Enter the elements no {i+1}:-"))
    ele.append(x)
for i in ele:
    if(i not in uniq):
        uniq.append(i)
    else:
        dupli.append(i)
print(f"The element in the list is {ele}\n\nThe unique element in the list is {uniq}\n\n"
      f"nThe duplicate element in the list is {dupli}")