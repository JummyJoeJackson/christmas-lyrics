import os
import random
import time
from colorama import Fore, Style
from lyrics import TREE, COLORS

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

def print_tree():
    # Print the star at the top
    print(COLORS[3] + TREE[0])
    # Print the rest of the tree
    for row in TREE[1:]:
        for char in row:
            if char == "*":
                # Randomly color the lights
                color = random.choice(COLORS)
                print(color + char, end="", flush=True)
            else:
                print(Fore.WHITE + char, end="", flush=True)
        print("")

def main():
    current_text = ""
    char_index = 0
    
    # Clean up the lyrics string to avoid initial empty newline if desired, 
    # but the triple quote string usually has one.
    full_text = LYRICS.strip()
    
    try:
        while True:
            # Clear the screen
            os.system("cls" if os.name == "nt" else "clear")
            
            # Print the animated tree
            print_tree()
            
            # Reset color for lyrics
            print(Style.RESET_ALL)
            
            # Print the lyrics generated so far
            # We print a few newlines to separate from the tree
            print("\n" + current_text)
            
            # Update the lyrics text
            if char_index < len(full_text):
                current_text += full_text[char_index]
                char_index += 1
            
            # Control the speed of animation and typing
            time.sleep(0.15)
            
    except KeyboardInterrupt:
        print("\n\nMerry Christmas!")

if __name__ == "__main__":
    main()
