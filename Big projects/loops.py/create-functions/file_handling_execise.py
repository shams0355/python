with open("readme.txt","w+") as f:
    f.write("my name is micheal jackson")
    f.seek(0)#what it doses that this function mean seek function when it is called to happen it will move the cursor to the begning of the context
    contex=f.read()
    print(contex)
if "jack"  in contex :
    print ("yes bro it is")  

