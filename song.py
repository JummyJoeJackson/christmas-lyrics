import os
import time
from pygame import mixer, error
from tree import print_tree

JINGLE_BELLS = """
🔔  🔔  🔔    🔔  🔔  🔔    🔔  🔔  🔔  🔔 🔔      
🎺  🎺  🎺    🎺  🎺  🎺  🎺🎺 🎺 🎺 🎺 🎺🎺
Dashing through the ❄️,
In a one-🐎 open 🛷,
Over the fields we go,
Laughing all the way
🔔 on bobtails ring,
Making 👻 bright,
What fun it is to ride & sing
A 🛷ing song tonight

Jingle 🔔, Jingle 🔔,
Jingle all the way
Oh what fun it is to ride
In a one-🐎 open 🛷

Jingle 🔔, Jingle 🔔,
Jingle all the way
Oh what fun it is to ride
In a one-🐎 open 🛷
"""

LAST_CHRISTMAS = """
🥁    🥁    🥁    🥁    🥁    🥁    🥁    🥁  
   🥁    🥁    🥁    🥁    🥁    🥁    🥁
Ah-huh, oooooh, ooooohhhhhhhhhhh, aaaaah, aaahhhhhhhhhhh,           
🥁  🥁  🥁  🥁🥁  🥁🥁
Last Christmas I gave you my 💕,
But the very next day, you gave it away       
This year, to save me from tears,
I'll give it to someone 𝓼𝓹𝓮𝓬𝓲𝓪𝓵
🥁 🥁🥁  🥁  🥁🥁 🥁🥁
Last Christmas I gave you my 💕,
But the very next day, you gave it away (gave it away)
This year, to save me from tears,
I'll give it to someone 𝓼𝓹𝓮𝓬𝓲𝓪𝓵 (𝓼𝓹𝓮𝓬𝓲𝓪𝓵)
"""

SONGS = {
    "1": LAST_CHRISTMAS,
    "2": JINGLE_BELLS,
}

SONG_NAMES = {
    "1": "last_christmas",
    "2": "jingle_bells",
}

def main():
    choice = input("What song do you want to play? (1, 2): ")

    if choice in SONG_NAMES:
        LYRICS = SONGS[choice]
        song_path = os.path.join("songs", f"{SONG_NAMES[choice]}.mp3")
    else:
        print("Invalid choice. Defaulting to Last Christmas.")
        LYRICS = SONGS["1"]
        song_path = os.path.join("songs", f"{SONG_NAMES["1"]}.mp3")

    # Initialize pygame mixer and play music
    mixer.init()
    try:
        mixer.music.load(song_path)
        mixer.music.play(-1)  # Loop indefinitely
    except error as e:
        print(f"Error playing music: {e}")
        time.sleep(2)

    current_text = ""
    char_index = 0

    full_text = LYRICS.strip()
    
    try:
        # Clear screen once initially
        os.system("cls" if os.name == "nt" else "clear")
        
        while True:
            # Move cursor to top-left
            print("\033[H", end="")
            
            # Print the animated tree
            print_tree()

            # Print the lyrics generated so far
            print("\n" + current_text)
            
            # Update the lyrics
            if char_index < len(full_text):
                current_text += full_text[char_index]
                char_index += 1
            
            # Control the speed of animation and typing
            time.sleep(0.11)

            
    except KeyboardInterrupt:
        print("\nMerry Christmas!")

if __name__ == "__main__":
    main()
