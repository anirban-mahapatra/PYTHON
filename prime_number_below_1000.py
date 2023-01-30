"""Problem:- Write a program to find the all prime numbers below 1000 using for loop."""

print("The prime numbers is:-",end=" ")
for i in range(1,1000):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i,end=" ")