"""Problem:- Write a Python program to print star pattern and reverse star pattern using Boolean variable"""

def star():
    n = int(input("Enter the number of lines you want:-"))
    for i in range(1, n+1):
        for j in range(0,i):
            print("*  ", end="")
        print("")


def rev_star():
    n = int(input("Enter the number of lines you want:-"))
    for i in range(0, n):
        for j in range(n-i,0,-1):
            print("*  ", end="")
        print("")

while(1):
    che=input("Enter 1 for star pattern, 0 for reverse and e for exit:-")
    if(che=='e' or che=='E'):
        break
    else:
        check=bool(int(che))

    if(check==True):
        star()
    elif(check==False):
        rev_star()

    else:
        print("\nInvalid Input\n")

print("Exit...")