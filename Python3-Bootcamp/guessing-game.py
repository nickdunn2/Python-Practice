import random

should_play = 'y'

while should_play == 'y':
    random_number = random.randint(1, 10)  # numbers 1 - 10
    user_input = 0
    guess_count = 0

    while user_input != random_number:
        user_input = int(input("Guess a number between 1 and 10: "))
        guess_count += 1

        if (user_input < random_number):
            print("Too low! Try again.\n")

        if (user_input > random_number):
            print("Too high! Try again.\n")

    guess_text = "guesses" if guess_count != 1 else "guess"
    print(f"You got it! It only took you {guess_count} {guess_text}.")
    should_play = input("\nWould you like to play again? (y/n) ")

print("\n\nThanks for playing!")
