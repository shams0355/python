print("project 0\nto print sum of first 10 natural numbers\nusing WHILE LOOP")
o=0
i=1
while (i<=10):
   o=o+i
   i=i+1
else:
  print("the sum of first 10 natural numbers are ",o)   
print('project 1\n print sum of first 10 natural numbers \nusing FOR LOOP ')
o=0
for i in range(1,11):
    o+=i
else:
    print(o)   
print("project 2") 
fact=1
print("factorial of the given number")
ask=int(input("enter the number you want factorial::-  "))
for i in range(ask,0,-1):
      fact*=i
else:
      print(fact)
print("project 3 \n print dimond")
for i in range(1,4):
    print("-"*(-i+3),end="")
    print("*"*((2*i)-1))
else:
 for u in range(3,1,-1):
    print("-"*(-u+4),end="")
    print("*"*(2*u-3)) 
print("project 4\nwelcome to custom square shapes")
ask=int(input("enter the length of side::-  "))
e=input("enter the boundary character::- ")
for i in range(1,ask+1):
    if (i==1) or (i==ask):
        print(f"{e*ask}")
    else:
        print(f"{e}",end="")
        print(" "*(ask-2),end="")
        print(e)