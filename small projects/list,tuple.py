#to clear the list
o=["Ali","Hamza","Arian","Wasay","Shaban","Kaleem","umer","Huzaifa","Maraj"]
print(o)
#in tuples
p=(1,2,3,4,5,4,3,6)
# p=list(p)
print(p)
for ao,bo in zip(o,p):#it doesn't print even the name of maraj cuz it has no value in the second lsit or tuple to make pair
    print(f"{ao} has got {bo} out of 10 numbers")

