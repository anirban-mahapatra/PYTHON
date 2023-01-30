"""Problem :- Write a Python program to get the difference between a given number and 10 if
the difference is positive then display the product of the given number and 10 otherwise
display their sum."""

num=int(input("Enter the number:-"))
diff=10-num
sum=10+num

if(diff>=0):
    print(f"The difference of {num} and 10(10-{num}) is {diff}")
else:
    print(f"The sum of {num} and 10(10+{num}) is {sum}")