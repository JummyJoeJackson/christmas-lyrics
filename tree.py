import os
import random
import time
from colorama import Fore

TREE = ["\n       *         ",
        "      ***        ",
        "     *****       ",
        "    *******      ",
        "   *********     ",
        "  ***********    ",
        " *************   ",
        "***************  ",
        "      |||        ",
        "     /|||\\       "]

COLORS = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.GREEN, Fore.GREEN]


def print_tree():
    print(COLORS[3] + TREE[0])
    for row in TREE[1:]:
        for char in row:
            if char == "*":
                color = random.choice(COLORS)
                print(color + char, end="", flush=True)
            else:
                print(Fore.WHITE + char, end="", flush=True)
        print("")
