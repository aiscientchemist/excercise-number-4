import random
print("Shall w e play a game?")
while True:
    x = input("choose (rock, paper, scissors): ")
    option = ["rock", "paper", "scissors"]
    computer = random.choice(option)
    if  x == computer:
        print("draw")
    elif x == "rock" and computer == "scissors":
        print("you win")
    elif x == "paper" and computer == "rock":
        print("you win")
    elif x == "scissors" and computer == "paper":
        print("you win")
    else:
        print("you lose")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break
    else:
        continue
