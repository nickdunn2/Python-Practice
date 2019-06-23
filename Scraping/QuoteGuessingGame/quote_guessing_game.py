# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    print(f"\nHere's a quote: {quote['text']}\n")
    print(quote["author"])
    guess = ''
    remaining_guesses = 4

    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(
            f"Who said this? (Guesses remaining: {remaining_guesses}) ")

        if guess.lower() == quote["author"].lower():
            print("\nBingo! You got it right!")
            break

        remaining_guesses -= 1
        print_hint(quote, remaining_guesses)

    play_again = ''

    while play_again.lower() not in ('y', 'yes', 'n', 'no'):
        play_again = input("Would you like to play again? (y/n) ")

    if play_again.lower() in ('y', 'yes'):
        return start_game(quotes)
    else:
        print("Okay, thanks for playing!")


def print_hint(quote, remaining_guesses):
    if remaining_guesses == 3:
        res = requests.get(quote["bio-link"])
        soup = BeautifulSoup(res.text, "html.parser")
        birthdate = soup.select_one("span.author-born-date").get_text()
        birthplace = soup.select_one(
            "span.author-born-location").get_text()
        print(
            f"\nHere's a hint: This person was born on {birthdate} {birthplace}\n")
    elif remaining_guesses == 2:
        print(
            f"\nHere's another hint: Their first name starts with: {quote['author'][0]}\n")
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[-1][0]
        print(
            f"\nOne final hint! Their last name starts with: {last_initial}\n")
    else:
        print(f"\nSorry, no more guesses! ({quote['author']} said this.)")


quotes = read_quotes("quotes.csv")
start_game(quotes)
