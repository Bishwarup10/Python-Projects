import random

user_wins = 0
computer_wins = 0

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            user_wins += 1
        else:
            print("Paper covers rock! You lose.")
            computer_wins += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            user_wins += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_wins += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            user_wins += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_wins += 1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print(f"\nGame ended. You won {user_wins} times. Computer won {computer_wins} times.")

