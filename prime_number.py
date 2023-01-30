"""Problem:- Write a program to find whether the given number is a prime numbers or not."""

num=int(input("Enter the number:-"))
for i in range(2,num):
    if (num%i==0):
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")