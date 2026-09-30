# def fact(n):
#     if (n==1) or(n==0):
#         return 1
#     return n*fact(n-1)
# a=fact(7)
# print(a)
# def odd(n):
#     if (n==1) or (n==0):
#         return 1
#     return n*odd(n-2)


# print("the type factorial of number is",odd(8))
#lets print an ice cream:
o=1
e=0
for i in range(1,8):
    if i==1:
        print("  ",end="")
        print("*"*4)
    elif i==2:
        print(" ",end="")
        print("*",end="")
        print("    ",end="")
        print("*")
    elif i==3:
        print("*"*8)   
    else:
        print(" "*e,end="")
        print("*",end="")
        print(" "*(7-o),end="")
        print("*")      
        o+=2
        e+=1
            
        