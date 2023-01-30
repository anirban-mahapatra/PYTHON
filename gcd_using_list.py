"""Problem:- Write a program to calculate GCD of two numbers using list."""

a=int(input("Enter the first element:-"))
b=int(input("Enter the second element:-"))
ls_a=[]
ls_b=[]

for i in range(1,a+1):
    if a%i==0:
        ls_a.append(i)

for j in range(1,b+1):
    if b%j==0:
        ls_b.append(j)

len_a=len(ls_a)
len_b=len(ls_b)
ans=[]

for k in range(1,len_a):
    for l in range(1,len_b):
        if ls_a[k]==ls_b[l]:
            ans.append(ls_a[k])
            break

len_ans=len(ans)
print("The GCD is:",ans[(len_ans)-1])