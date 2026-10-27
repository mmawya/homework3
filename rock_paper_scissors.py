import random

user = input("choose rock(R), paper(P), or scissors(S): ").upper()
computer = random.choice(["R", "P", "S"])

print("computer chose:", computer)

if user not in ["R", "P", "S"]:
    print("invalid input. Please choose R, P, or S.")
else:
    if user == computer:
        print("It's a tie!")
    elif (user == "R" and computer == "S") or (user == "P" and computer == "R") or (user == "S" and computer == "P"):
        print("You win!")
    else:
        print("Computer wins!")