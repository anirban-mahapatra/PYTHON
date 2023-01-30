"""Problem:- Write a program to find Fibonacci numbers."""

def fibo(num):
    a=0
    b=1
    print("The fibonacci siries is:-",end=' ')
    if(num==1):
        print(a)
    else:
        print(a,',',b,',',end=' ')
        for i in range(2,num):
            c=a+b
            a=b
            b=c
            print(c,end=' ')
            if(i==num-1):
                break
            else:
                print(end=' , ')

num=int(input("Enter the number of terms you want to see in fibonacci series:-"))
fibo(num)