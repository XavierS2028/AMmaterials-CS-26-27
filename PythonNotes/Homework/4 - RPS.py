# RPS.py
import random

computerPlay = random.randint(0, 4)
playNames = ["Scissor", "Rock", "Paper", "Lizard", "Spock"]

userPlay = int(input(
"""What is your move?
    Scissor - 0
    Rock    - 1
    Paper   - 2
    Lizard  - 3
    Spock   - 4
> """))

computerString = playNames[computerPlay]
userString     = playNames[userPlay]

if computerPlay == userPlay:
    print(f"The computer is {computerString}. You are {userString} too. It is a draw.")
else:
    print(f"The computer is {computerString}. You are {userString}. ", end="")
   
    if userPlay == 0:
        if (computerPlay == 3) or (computerPlay == 2):
            print(f"You won.")
        else:
            print(f"You lost.")
    elif userPlay == 1:
        if (computerPlay == 3) or (computerPlay == 0):
            print(f"You won.")
        else:
            print(f"You lost.")
    elif userPlay == 2:
        if (computerPlay == 4) or (computerPlay == 1):
            print(f"You won.")
        else:
            print(f"You lost.")
    elif userPlay == 3:
        if (computerPlay == 4) or (computerPlay == 2):
            print(f"You won.")
        else:
            print(f"You lost.")
    elif userPlay == 4:
        if (computerPlay == 0) or (computerPlay == 1):
            print(f"You won.")
        else:
            print(f"You lost.")