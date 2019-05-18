from random import randint

print("Welcome to Rock, Paper, Scissors!\n")
series_length = None
allowed_series_length = [3, 5, 7]

while series_length not in allowed_series_length:
    series_length = int(
        input("Would you like to play Best Of 3, Best Of 5, or Best Of 7? (3/5/7) "))


player_wins = 0
computer_wins = 0
winning_score = series_length // 2 + 1

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player: {player_wins} | Computer: {computer_wins}\n")
    print("...rock...")
    print("...paper...")
    print("...scissors...\n")

    player = input("Enter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    random_num = randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}\n")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!\n")
    print(f"FINAL SCORE -- Player: {player_wins} | Computer: {computer_wins}")
elif player_wins == computer_wins:
    print("IT'S A TIE")
    print(f"FINAL SCORE -- Player: {player_wins} | Computer: {computer_wins}")
else:
    print("OH NO :( THE COMPUTER WON...")
    print(f"FINAL SCORE -- Player: {player_wins} | Computer: {computer_wins}")
