import random
import pyttsx3
y=random.randint(1,100)
while True:
    k=int(input(f"Enter a number which is less than {y}::-"))
    if k<y:
        print ("YEA ",k," is less than ",y,"\nCONGRATULATIONS")
        v=pyttsx3.init()
        v.say("Thanks for interacting with me")
        v.runAndWait()
        break
    else:
        print(f"Are you in your senses {k} is not less than {y}\nTRY AGAIN")
    
