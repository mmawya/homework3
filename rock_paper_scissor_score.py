import random

user_score = 0
computer_score = 0
ties = 0

while True:
    user = input("Choose Rock (R), Paper (P), or Scissors (S): ").upper()

    if user not in ["R", "P", "S"]:
        print("Invalid choice!")
        continue

    computer = random.choice(["R", "P", "S"])

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
        ties += 1

    elif (user == "R" and computer == "S") or \
         (user == "P" and computer == "R") or \
         (user == "S" and computer == "P"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)
    print("Ties:", ties)

    again = input("Do you want to play again? (yes/no): ").lower()

    if again != "yes":
        break

print("Final score:")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Ties:", ties)
print("Game over!")