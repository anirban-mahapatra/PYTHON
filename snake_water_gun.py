"""Snake water gun:- Create a snake water gun game in Python!
Search Snake water gun game in google if you need help on rules and how to play the game!
"""

import random

print("\nWellcome to SNAKE WATER GAN game\n")
c=0;y=0;i=0

while(i!=10):
    i=i+1
    print(f"Chance no {i}\n{10-i} time left\n")
    l=["Snake","Water","Gun"]
    choice=random.choice(l)
    while True:
        a=input("s for Snake\nw for water\ng for gun\nEnter your choice:-")
        if(a=="s" or a=="w" or a=="g"):
            ani=a.upper()
            break
        else:
            print("You enter wrong input\n")

    print("\nComputer choice is",choice,"\n")
    if (choice=="Snake"):
        if (ani=="S"):
            c=c+1;y=y+1
            print(f"Draw this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="W"):
            c=c+1
            print(f"Computer win this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="G"):
            y=y+1
            print(f"You win this time\nScore:-\nComputer={c}\nYou={y}\n")
    if (choice=="Water"):
        if (ani=="S"):
            y=y+1
            print(f"You win this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="W"):
            c = c + 1;y = y + 1
            print(f"Draw this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="G"):
            c = c + 1
            print(f"Computer win this time\nScore:-\nComputer={c}\nYou={y}\n")
    if (choice=="Gun"):
        if (ani=="S"):
            c = c + 1
            print(f"Computer win this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="W"):
            y = y + 1
            print(f"You win this time\nScore:-\nComputer={c}\nYou={y}\n")
        elif(ani=="G"):
            c = c + 1;y = y + 1
            print(f"Draw this time\nScore:-\nComputer={c}\nYou={y}\n")
if (y>c):
    print("\nYOU IS WIN THE GAME\n")
elif(c>y):
    print("\nCOMPUTER WIN THE GAME\n")
else:
    print("\nTHE GAME IS DRAW\n")