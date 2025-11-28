import random
import shutil
from colorama import Fore


TREE = ["\n       *       ",
        "      ***      ",
        "     *****     ",
        "    *******    ",
        "   *********   ",
        "  ***********  ",
        " ************* ",
        "***************",
        "      |||      ",
        "     /|||\\     "]

COLORS = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.GREEN, Fore.GREEN]

COLUMNS = shutil.get_terminal_size().columns


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
    padding = max(0, (COLUMNS - 15) // 2)
    pad_str = " " * padding
    
    final_str = ""
    for line in get_tree_string().split('\n'):
        #if line: 
        final_str += pad_str + line + "\n"
    
    print(final_str, end="")
