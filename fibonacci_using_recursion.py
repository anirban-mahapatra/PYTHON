"""Problem:- Write a program to find Fibonacci numbers using recursive function."""

def fibo(no):
    if(no<=1):
        return no
    else:
        return (fibo(no-1)+fibo(no-2))

no=int(input("Enter the namber of terms you want to see in fibonacci series:-"))
print("Fibonacci series is:-",end="")
for i in range(no):
    print(fibo(i),end=" ")
    if (i==no-1):
        break
    else:
        print(end=' , ')