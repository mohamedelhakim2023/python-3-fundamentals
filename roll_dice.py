# using random library to roll a dice
import random

roll = random.randint(1, 6)

guess = int(input("Guess the number:  \n"))

if guess == roll:
    print("You win")
else:
    print("You lose")
    print("The number was: ", roll)
