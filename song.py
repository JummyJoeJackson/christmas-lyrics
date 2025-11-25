import os
import random
import time
from colorama import Fore
from tree import TREE, COLORS, print_tree

LYRICS = """
Jingle bells, jingle bells,
Jingle all the way.
Oh! what fun it is to ride
In a one-horse open sleigh.
Hey!
Jingle bells, jingle bells,
Jingle all the way;
Oh! what fun it is to ride
In a one-horse open sleigh.
"""

def main():
    current_text = ""
    char_index = 0

    full_text = LYRICS.strip()
    
    try:
        while True:
            # Print the animated tree
            print_tree()

            # Print the lyrics generated so far
            print("\n" + current_text)
            
            # Update the lyrics
            if char_index < len(full_text):
                current_text += full_text[char_index]
                char_index += 1
            
            # Control the speed of animation and typing
            time.sleep(0.1)

            # Clear the screen
            os.system("cls" if os.name == "nt" else "clear")
            
    except KeyboardInterrupt:
        print("\nMerry Christmas!")

if __name__ == "__main__":
    main()
