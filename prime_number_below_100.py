"""Problem:- Write a program to find the all prime numbers below 100 using function."""

def prime():
    for i in range(1,100):
        for j in range(2,i):
            if (i%j==0):
                break
        else:
            print(i, end=" ")

print("The prime numbers is:-",end=" ")
prime()