import os
import random
import time
from colorama import Fore


def print_tree():
    tree = ["\n       *         ",
            "      ***        ",
            "     *****       ",
            "    *******      ",
            "   *********     ",
            "  ***********    ",
            " *************   ",
            "***************  ",
            "      |||        ",
            "     /|||\\       "]

    colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.GREEN, Fore.GREEN]

    print(colors[3] + tree[0])
    for row in tree[1:]:
        for char in row:
            if char == "*":
                color = random.choice(colors)
                print(color + char, end="", flush=True)
            else:
                print(Fore.WHITE + char, end="", flush=True)
        print("")


if __name__ == "__main__":
    while True:
        print_tree()
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")
