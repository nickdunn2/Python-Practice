# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

base_url = "https://www.rithmschool.com"
path = "/blog"

with open("rithm_blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])

    while path:
        res = requests.get(base_url + path)
        print(f"Scraping from {base_url + path}...")
        soup = BeautifulSoup(res.text, "html.parser")
        articles = soup.find_all("article")

        for article in articles:
            a_tag = article.select_one("h4.section-heading > a")
            title = a_tag.get_text()
            href = base_url + a_tag["href"]
            date = article.find("time")["datetime"]
            csv_writer.writerow([title, href, date])

        # If there's a Next button, keep going
        next_button = soup.select_one("span.next")
        path = next_button.find("a")["href"] if next_button else None
        sleep(1)
