"""Problem:- Write a program to find n-th Fibonacci numbers using function"""

def fibo(term):
    a=0
    b=1
    c=0
    if (term == 1):
        return a

    elif (term == 2):
        return b

    else:
        for i in range(2, term):
            c = a + b
            a=b
            b=c
        return c

term=int(input("Enter the number of term:-"))
print(f"The {term} no element in fibonacci series is ",fibo(term))
