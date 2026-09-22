# ask = int(input("Enter the size of hollow diamond: "))

# for i in range(1, 2 * ask):   # single loop for both halves
#     if i <= ask:
#         spaces = ask - i
#         inner = 2 * i - 3
#     else:
#          spaces = i - ask
#          inner = 2 * (2 * ask - i) - 3

#     print(" " * spaces, end="")
#     if inner < 0:
#         print("*")   # top and bottom points
#     else:
#         print("*" + " " * inner + "*")
#to make functions
# def pakistan():
#     print("kia hua bhai")
# pakistan()
# def summ():
#     a=int(input("enter a::-"))
#     b=int(input("enter b::-"))
#     print("their b summ",a-(a+b))
# print("summ",summ())
def  s():
    a=int(input("enter the a "))
    b=int(input("enter the b "))
    
    sum=a+b*34
    return print("sum==",sum)

s()
