import os
import random
import time
from pygame import mixer, error
from colorama import Fore
from tree import TREE, COLORS, print_tree

LYRICS = """
Dashing through the snow,
In a one-horse open sleigh,
Over the fields we go,
Laughing all the way.
Bells on bobtails ring,
Making spirits bright,
What fun it is to ride and sing
A sleighing song tonight.
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
    # Initialize pygame mixer and play music
    mixer.init()
    try:
        song_path = os.path.join("songs", "jingle_bells.mp3")
        mixer.music.load(song_path)
        mixer.music.play(-1)  # Loop indefinitely
    except error as e:
        print(f"Error playing music: {e}")
        time.sleep(2)

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
            time.sleep(0.05)

            # Clear the screen
            os.system("cls" if os.name == "nt" else "clear")
            
    except KeyboardInterrupt:
        print("\nMerry Christmas!")

if __name__ == "__main__":
    main()
