import random

compu_choice = random.choice(["paper", "rock", "scissor"])
user_choice = input("Do you want to choose paper, rock or scissor? ")

if compu_choice == user_choice:
    print("Tie")
elif compu_choice == "paper" and user_choice == "rock":
    print("Computer wins")
elif compu_choice == "rock" and user_choice == "scissor":
    print("Computer wins")
elif compu_choice == "scissor" and user_choice == "paper":
    print("Computer wins")
elif compu_choice == "rock" and user_choice == "paper":
    print("You win")
elif compu_choice == "scissor" and user_choice == "rock":
    print("You win")
elif compu_choice == "paper" and user_choice == "scissor":
    print("You win")
else:
    print("Invalid input")
