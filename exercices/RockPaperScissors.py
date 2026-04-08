# Create a rock paper scissors game
# The user will choose rock, paper, or scissors 
# Each player enter their name and then the game begins

# Each player takes turns and the program determines the winner and give 1 pt to the winner
# The first player to reach 3 pts wins the game
import random
options = {"1": "rock", "2": "paper", "3": "scissors"}
player1 = input("Player 1, enter your name: ")
# player2 = input("Player 2, enter your name: ")
player2 = "CPU"
score1 = 0
score2 = 0

while score1 < 3 and score2 < 3:
    while True:
        choice1 = input(f"{player1}, choose 1 (rock), 2 (paper), or 3 (scissors): ")
        if choice1 in options:
            choice1 = options[choice1]
            break
        print("Invalid selection. Please enter 1, 2, or 3.")

    # while True:
    #     choice2 = input(f"{player2}, choose 1 (rock), 2 (paper), or 3 (scissors): ")
    #     if choice2 in options:
    #         choice2 = options[choice2]
    #         break
    #     print("Invalid selection. Please enter 1, 2, or 3.")
    cpuChoice = random.randint(1, 3)
    choice2 = options[str(cpuChoice)]

    print(f"{player1} chose {choice1}")
    print(f"{player2} chose {choice2}")

    if choice1 == choice2:
        print("It's a tie!")
    elif (choice1 == "rock" and choice2 == "scissors") or (choice1 == "paper" and choice2 == "rock") or (choice1 == "scissors" and choice2 == "paper"):
        print(f"{player1} wins!")
        score1 += 1
    else:
        print(f"{player2} wins!")
        score2 += 1
    print(f"{player1}: {score1} - {score2} {player2}")
if score1 == 3:
    print("Player 1 wins!")
if score2 == 3:
    print("Player 2 wins!")