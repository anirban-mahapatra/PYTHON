"""Problem-7: Write a program to compute the following sum using function:
            1 + (1+2) + (1+2+3) + (1+2+3+4) + ..... ..... .... up to 10 terms."""

def sum(term):
    num = 0
    for i in range(1,term+1):
        for j in range(1,i+1):
            num=num+j
    return num


term=10
print(f"The sum of {term} terms is {sum(term)}")