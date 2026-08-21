print("hello buddy lets paly a game \nA game in which you have to guess the  a randon numbere between 1 and 100")
ask=input("if  you are ready then press ENTER key to statr the game")
import random 
low=1
high=100
number=random.randint(low,high)
print(number)  
while True:
 confirm=input("is this the number you gussed? YES OR NO")
 if confirm=="yes":
    print("I CAN READ YOUR MIND BRO HAHAHA")
    break
 else :
    tell=input("ok tell me if the number which have guess is less than your guessed number or more:: ")
    if tell=="more":
      high=number-1
      
    else:
      low=number+1
    number=random.randint(low,high)
    print(number)
       

    