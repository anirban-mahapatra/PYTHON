"""Problem:- Write a program to compute half of a list"""

ls=["Apple","Banana","Watermelon",12,30,55]
l1=[]
l2=[]
len=len(ls)
len1=0
if len%2==0:
    len1=len//2
else:
    len1=(len+1)//2

for i in range(len1):
    l1.append(ls[i])
for j in range(len1,len):
    l2.append(ls[j])

print("The main lis is ",ls)
print("\nThe first half of the main list is ",l1)
print("\nThe second half of the main list is ",l2)