import random
from colorama import Fore, init


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


def get_tree_string():
    tree_str = COLORS[3] + TREE[0] + "\n"
    for row in TREE[1:]:
        for char in row:
            if char == "*":
                color = random.choice(COLORS)
                tree_str += color + char
            else:
                tree_str += Fore.WHITE + char
        tree_str += "\n"
    return tree_str

def print_tree():
    print(get_tree_string(), end="")

