import os
import random
import time
from colorama import Fore


def print_tree():
    tree = ["               ",
            "       *       ",
            "      ***      ",
            "     *****     ",
            "    *******    ",
            "   *********   ",
            "  ***********  ",
            " ************* ",
            "***************",
            "      |||      ",
            "     /|||\\     "]
    colors = [Fore.RED, Fore.GREEN, Fore.GREEN, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA]
    for row in tree:
        for char in row:
            if char == "*":
                color = random.choice(colors)
                print(color + char, end="", flush=True)
            else:
                print(char, end="", flush=True)
                print(Fore.LIGHTBLACK_EX, end="", flush=True)
        print("")


if __name__ == "__main__":
    while True:
        print_tree()
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")