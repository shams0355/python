import time
import pyttsx3


ask = input("Enter your name::")
voice = pyttsx3.init()

# First two voice commands
voice.say(f"Hello {ask}, nice to meet you, how are you doing today")
voice.say("Hope that you are all right. Ok, let me know which number's multiplicative table you want")
voice.runAndWait()
time.sleep(1)

print("Which number's multiplicative table do you want to print?")  # to support the voice command
k = int(input("Enter that number whose multiplicative table you want::-"))
voice.stop()


# Third voice command
voice.say(f"Ooh {ask}, you want {k}'s table, press enter to see the table ::")
voice.runAndWait()   # <-- Make sure this completes before moving on
time.sleep(1)
o=input("Press enter to see the table::")

# Speak and print the table
for i in range(1, 11):
    line = f"{k} x {i} = {i*k}"
    print(line)
    
