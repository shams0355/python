classes=["class 5th","class 6th","class 7th","class 8th"]
marks=[]
names=[]
print("                \033[1mWELCOME TO THE NEWYORK STARS\033[0m")
for elements in classes:
    name=input(f"ENTER THE NAME OF YOUR BROTHER STUDYING IN {elements.upper()} ::-  ").upper()
    names.append(name)
print("                \033[1mOK BROTHER! NOW ENTER THEIR MARKS\033[0m")    
for nam,cla in zip(names,classes):
    ask=int(input(f"ENTER THE MARKS OF YOUR BROTHER {nam} who is studying in {cla.upper()} ::- "))
    marks.append(ask)
print("                \033[1mOK CHECK BELOW I CREATED THE LSIT\033[0m")    
for n,c,m in zip(names,classes,marks):
    print(f"Marks of {n} in {c.upper()} are {m} ")    
print(zip(names,classes,marks))
P=input("PRESS THE ENTER BUTTON IF IT IS CORRECT")
print("\033[1mTHANKS FOR USING OUR WEBSITE")