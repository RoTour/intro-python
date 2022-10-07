import random

rand = random.randint(1, 100)
nbTry = 10
userTry = None

while userTry != rand and nbTry > 0:
    userTry = int(input(f"Find a number between 1 and 100. You have {nbTry} tries left: "))
    if userTry < rand:
        nbTry -= 1
        print("Too low")
    elif userTry > rand:
        nbTry -= 1
        print("Too high")

if nbTry > 0:
    print("You win!")
else:
    print("You lose!")