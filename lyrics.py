from colorama import Fore

print(Fore.GREEN + "Merry Christmas!")


tree = ["       *       ",
        "      ***      ",
        "     *****     ",
        "    *******    ",
        "   *********   ",
        "  ***********  ",
        " ************* ",
        "***************",
        "       ||      ",
        "      /||\\     "]

def print_tree():
    for row in tree:
        print(row)

print_tree()