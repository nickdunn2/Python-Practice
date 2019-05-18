from pyfiglet import figlet_format
from termcolor import colored

allowed_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")


def get_colored_ascii_art(text, color):
    if color not in allowed_colors:
        color = "blue"

    ascii_msg = figlet_format(text)
    colored_ascii = colored(ascii_msg, color)

    return colored_ascii


msg = input("what message do you want to print? ")
color = input("what color? ").lower()


print(get_colored_ascii_art(msg, color))
