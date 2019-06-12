# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep

# Set up
base_url = "http://quotes.toscrape.com"
path = "/"
all_quotes = []

while path:
    # Grab data
    res = requests.get(base_url + path)
    print(f"Now scraping {base_url + path}...")
    soup = BeautifulSoup(res.text, "html.parser")
    quotes = soup.select("div.quote")

    # Loop through and append to all_quotes list
    for quote in quotes:
        all_quotes.append({
            "quote": quote.select_one("span.text").get_text(),
            "author": quote.select_one(".author").get_text(),
            "bio-link": base_url + quote.find("a")["href"]
        })

    # If there's a Next button, keep going
    next_button = soup.select_one(".pager > .next")
    path = next_button.find("a")["href"] if next_button else None
    sleep(1)


print(all_quotes)
