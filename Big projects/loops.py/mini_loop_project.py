#first shape
print("WANT TO PRINT TRIANGLE")
ask=int(input("ENTER TRIANGLE'S WIDTH"))
for i in range(1,ask+1):
    if i==ask:
        print("* "*ask)
    else:
       if i==1:
         print(" "*(ask-i),end="")
         print("*")
       else:  
          print(" "*(ask-i),end="")
          print("*",end="")
          print(" "*(2*i-3),end="")
          print("*")





