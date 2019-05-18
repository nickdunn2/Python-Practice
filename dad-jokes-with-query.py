from requests import get
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

print(colored(figlet_format("Dad Jokes 3000"), "green"))

base_url = "https://icanhazdadjoke.com/search"
search_term = input("Let me tell you a joke! Give me a topic: ")

data = get(
    base_url,
    headers={"Accept": "application/json"},
    params={"term": search_term}
).json()

total_jokes = data["total_jokes"]
jokes = [result["joke"] for result in data["results"]]
is_plural = search_term[-1] == "s"
term_text = f"a {search_term}" if not is_plural else search_term

if not jokes:
    output = f"Sorry, I don't have any jokes about {term_text}! Please try again."
elif total_jokes == 1:
    output = f"I've got one joke about {term_text}. Here it is:\n\n{choice(jokes)}\n"
elif total_jokes > 1:
    output = f"I've got {len(jokes)} jokes about {term_text}. Here's one:\n\n{choice(jokes)}\n"
else:
    output = "Something went wrong. Please try again."

print(output)
