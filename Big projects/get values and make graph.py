import matplotlib.pyplot as plt
subjects=["urdu","english","math","physics","computer","pak studies"]
marks=[]
for sub in subjects:
    a=int(input(f"ENTER THE MARKS YOU OBTAINED IN {sub.upper()} OUT OF 100 ::-  "))
    marks.append(a)
plt.bar(subjects,marks,color="green")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")
plt.title("HIGHEST MARKS GRAPH")
plt.show()