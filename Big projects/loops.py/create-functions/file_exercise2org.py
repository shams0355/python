import random
import os

def game():
    print("You are in game mode")
    score = random.randint(1, 100)

    # Full path to file
    filepath = r"C:\Users\hp\OneDrive\Desktop\python\Big projects\loops.py\create-functions\hiscore.txt"

    # Read old high score
    if os.path.exists(filepath):
        with open(filepath, "r") as l:
            content = l.read().strip()
            # if content!="":
            #     content=int(content)
            # else:
            #     content=0    
            high_score = int(content) if content else 0
    else:
        high_score = 0

    # Compare and update
    if score > high_score:
        print("🎉 New High Score!")
        with open(filepath, "w") as f:
            f.write(str(score))
        print("Your high score is", score)
    else:
        print("Your high score is", high_score)

    return score

game()