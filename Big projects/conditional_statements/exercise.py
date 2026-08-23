import matplotlib.pyplot as plt
subjects=[]
dictionary={}
marks=[]
si=["1st","2nd","3rd","4th","5th","6th","7th","8th"]
ask=int(input("HOW MANY SUBJECTS YOU HAVE::-  "))
for i in range(ask):
     add_subject=input(f"ENTER THE NAME OF YOUR {si[i]} SUBJECT::- ").upper()#thats a very critical logic , thats the logic man ,what are you thinking
     subjects.append(add_subject)
     
for i in range(ask) :
     add_marks=int(input(f"ENTER YOUR MARKS IN {subjects[i]} ::- "))
     marks.append(add_marks)
for a,s in zip(subjects,marks)  :
        dictionary.update({a:s})
a=0 
b=100000      
print(dictionary) 
for i,o in dictionary.items():
      if o>a :
            a=o
            t=i
for k,g in dictionary.items():
      if g<b :
            b=g
            f=k
            
      
# print(min(dictionary))       
print(f"YOU  HAVE GAINED HIGHEST MARKS  WHICH ARE {a} IN {t}")
print(f"YOU  HAVE GAINED LOWEST MARKS WHICH ARE {b} IN {f}")
ask2=input("if you want to see it visually then write \"y\" other wise any key::-- ")
if ask2=="y":
      plt.bar(subjects,marks,color="skyblue",edgecolor="black")
      plt.xlabel("SUBJECTS")
      plt.ylabel("MARKS")
      plt.title("SUBJECT-MARKS CHART")
      plt.grid(axis="y",linestyle="--",alpha=0.7)
      plt.show()
   