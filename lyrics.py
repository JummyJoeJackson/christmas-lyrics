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

    for i in range(len(tree)):
        if i % 2 == 0:
            print(Fore.RED + tree[i], flush=True)
        else:
            print(Fore.GREEN + tree[i], flush=True)


print(Fore.GREEN + "Merry Christmas!\n", flush=True)
print_tree()

# loading . . . function'
def loading():
    print(".", flush=True)