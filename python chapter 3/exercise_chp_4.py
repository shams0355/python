#FIRST EXERCISE
category=["fruit","color","animal","bird"]
favourite=[]
print("\033[1mWELCOME SIR , HOPE YOU ARE FINE\033[0m \nOK NAME YOUR FAVOURITE THINGS ")
for items in category:
 fav=input(f"ENTER THE NAME OF YOUR FAVOURITE {items.upper()} ")
 favourite.append(fav)
print("your favourite things list is here::- ",favourite)
for cat,fav in zip(category,favourite):
 print(f"{fav} is your favourite {cat}")