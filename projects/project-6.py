#it will print the factorial of the number!
num=int(input("enter a number you want to print the factorial of ::  "))
fact=1
for i in range(num,0,-1):
    fact*=i
print(f"the factorial of number {num}! is {fact} ")    