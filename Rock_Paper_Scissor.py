"""Rock-Paper-Scissors Game: This is a classic game that
can be easily implemented in Python. You can write a program
that allows the user to play against the computer, where the
computer makes a random choice and compares it to the user's
choice to determine a winner."""

import random

# 1. list of options:
options = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']

# 2.  Ask player Name
name = input("What's your name?")

# 3. Initialize Score
ComputerScore = 0
PlayerScore = 0
NumberOfRounds = 0

# 4. Set gameOn flag to True
gameOn = True
# f = firstletter to big ones
print(f"Welcome {name.title()}")

# 5. Loop: while gameOn flag is true repeat 6 - 12
# 6. Random: randomly generate one option from the list as Computer
while gameOn:
    ComputerOption = random.choice(options)

    # 7. Player option: Let player choose an option and set it ti PlayerOption
    PlayerOption = input("Enter Rock/Paper/Scissor/Lizard/Spock :").title()
    # 8. Rounds: ++
    NumberOfRounds += 1

    print(f"Computer Option : {ComputerOption}")
    print(f"{name.title()} option : {PlayerOption}")

    # 9. Outcome: If goth computer and player have same outcome it is a draw. If not then proceed to step 10
    if ComputerOption == PlayerOption:
        print("Draw")

    # 10. Winner: based on rules increase winner score by 1
    elif (ComputerOption == "Rock" and PlayerOption == "Scissor") \
            or (ComputerOption == "Scissor" and PlayerOption == "Paper") \
            or (ComputerOption == "Paper" and PlayerOption == "Rock") \
            or (ComputerOption == "Lizard" and PlayerOption == "Spock") \
            or (ComputerOption == "Spock" and PlayerOption == "Scissor") \
            or (ComputerOption == "Scissor" and PlayerOption == "Lizard") \
            or (ComputerOption == "Lizard" and PlayerOption == "Paper") \
            or (ComputerOption == "Paper" and PlayerOption == "Spock") \
            or (ComputerOption == "Spock" and PlayerOption == "Rock"):
        print("Computer wins")
        ComputerScore += 1
    elif (PlayerOption == "Rock" and ComputerOption == "Scissor") \
            or (PlayerOption == "Scissor" and ComputerOption == "Paper") \
            or (PlayerOption == "Paper" and ComputerOption == "Rock") \
            or (PlayerOption == "Lizard" and ComputerOption == "Spock") \
            or (PlayerOption == "Spock" and ComputerOption == "Scissor") \
            or (PlayerOption == "Scissor" and ComputerOption == "Lizard") \
            or (PlayerOption == "Lizard" and ComputerOption == "Paper") \
            or (PlayerOption == "Paper" and ComputerOption == "Spock") \
            or (PlayerOption == "Spock" and ComputerOption == "Rock"):
        print(f"{name.title()} wins")
        PlayerScore += 1
    else:
        print("Choose a valid option to play this game.")

    # 11. Score: Display updated score
    print("-------------------------")
    print("")
    print(f"Round No: {NumberOfRounds}")
    print("------ Score Board ------")
    print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
    print("===============================")
    print("")

    # 12. Rounds: If the amount of rounds is more than 5 set gameOn flag to false
    if NumberOfRounds > 5:
        GameOn = False
        break
# 13. Winner: Choose and display the final winner based on total score
if PlayerScore == ComputerScore:
    print("Tie!!")
elif PlayerScore > ComputerScore:
    print(f"Congrats {name.title()}, You won the game!!")
else:
    print(f"Oops computer won the game!! Get good {name.title()}!")
