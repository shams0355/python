#print stars  in ascending order
def stars(a,n):
    if a>n:
        return
    print(a*"*")
    a=a+1
    stars(a,n)
stars(1,6)
#global variable concept
def dummy():
    global a
    a=1
    return a
print(dummy())
print(a+1)
  
   
