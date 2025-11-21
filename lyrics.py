from colorama import Fore


# kinda self-explanatory
def print_tree():
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

    for row in tree:
        print(row)


print(Fore.GREEN + "Merry Christmas!\n")
print_tree()