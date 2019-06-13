# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import choice

# Set up
base_url = "http://quotes.toscrape.com"
path = "/"
all_quotes = []

# TODO: Store all this in a CSV so the scraping doesn't happen every time
while path:
    # Grab data
    res = requests.get(base_url + path)
    print(f"Now scraping {base_url + path}...")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.select("div.quote")

    # Loop through and append to all_quotes list
    for quote in quotes:
        all_quotes.append({
            "text": quote.select_one("span.text").get_text(),
            "author": quote.select_one(".author").get_text(),
            "bio-link": base_url + quote.find("a")["href"]
        })

    # If there's a Next button, keep going
    next_button = soup.select_one(".pager > .next")
    path = next_button.find("a")["href"] if next_button else None
    sleep(0.2)

quote = choice(all_quotes)
print(f"Here's a quote: {quote['text']}\n")
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
    if remaining_guesses == 3:
        res = requests.get(quote["bio-link"])
        soup = BeautifulSoup(res.text, "html.parser")
        birthdate = soup.select_one("span.author-born-date").get_text()
        birthplace = soup.select_one("span.author-born-location").get_text()
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

print("WHILE LOOP COMPLETE")
