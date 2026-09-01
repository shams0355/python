#problem no 1
print("to meet only with the persons whoes name starts with the letter s in a list")
names=["shams","zarar","ali","saima","zulfiqar","samiullah"]
for every_name in names:
    if every_name.startswith("s"):
        print("hello"   ,every_name)
#problem no 2
print("to print table using while loop")
ask=input("enter the number which you want to see its table upto 30")
ask=int(ask)
i=1
while i<31:
    print(f"{ask} x {i} = {i*ask}")
    i=i+1
#problem no 3
#to check whether the input number is a prime number or not
print("to check whether the input number is a prime number or not")
ask=int(input("PLEASE ENTER A PRIME NUMBER::-  "))
count=0
for i in range(1,ask+1):
    if ask%i==0:
        count+=1
if count==2:
    print(ask," is a prime number")   
else :
    print(ask," it is not a prime number ")         
