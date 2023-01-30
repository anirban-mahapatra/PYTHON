"""You have to build a Number Guessing Game, in which a winning number is set to some integer value.
The Program should take input from the user, and if the entered number is less than the winning number,
a message should display that the number is smaller and vice versa.

Instructions:
1. The number of guesses should be limited, i.e (5 or 9).
2. Print the number of guesses left.
3. Print the number of guesses he took to win the game.
4. Game Over message should display if the number of guesses becomes equal to 0."""

num=18
i=0
while(i<=9):
    print("Your number of guess is ",i)
    n=int(input("Enter the number:-"))
    if n==num:
        print("You enter right number.\nYour number of chance is ",i)
        break
    elif n>num:
        print("Your number is getter then the number.\nYou have",(9-i),"chance more")
    else:
        print("Your number is less then the number.\nYou have",(9-i),"chance more")
    i=i+1
if i==9:
    print("You attend maximum chance.\n\n\tGAME OVER")