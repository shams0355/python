import random
i=0
total=[]
value_dict={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9}
high_score=[]
while True:
 while i<3:
    numbers=[random.randint(1,10) for i in range(1,11)]
    # print(numbers)
    choose=input("choose a letter in range of A--j ::-  ")
    total.append(numbers[value_dict[choose]])
    print("your number is ",numbers[value_dict[choose]])
    i+=1
 i=0   
 print("GAME OVER")
 print("your score is ",sum(total))   
 high_score.append(sum(total))
 ask=input("do you want to play the game again ::- ").lower()
 if ask=="no":
   break 
print("high score in your game is",max(high_score))
