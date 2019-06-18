# http://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

# Set up
BASE_URL = "http://quotes.toscrape.com"


# TODO: Store all this in a CSV so the scraping doesn't happen every time
def scrape_quotes():
    all_quotes = []
    path = "/"

    while path:
        # Grab data
        res = requests.get(BASE_URL + path)
        print(f"Now scraping {BASE_URL + path}...")
        soup = BeautifulSoup(res.text, "html.parser")
        quotes = soup.select("div.quote")

        # Loop through and append to all_quotes list
        for quote in quotes:
            all_quotes.append({
                "text": quote.select_one("span.text").get_text(),
                "author": quote.select_one(".author").get_text(),
                "bio-link": BASE_URL + quote.find("a")["href"]
            })

        # If there's a Next button, keep going
        next_button = soup.select_one(".pager > .next")
        path = next_button.find("a")["href"] if next_button else None
        sleep(1)

    return all_quotes


def write_quotes_to_csv(quotes):
    with open("quotes.csv", "w") as csvfile:
        headers = ["text", "author", "bio-link"]
        csv_writer = DictWriter(csvfile, fieldnames=headers)
        csv_writer.writeheader()

        for quote in quotes:
            csv_writer.writerow(quote)


quotes = scrape_quotes()
write_quotes_to_csv(quotes)
