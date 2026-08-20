# 🛒 Project Idea: Smart Shopping Cart System
# 🎯 Goal
# Build a program that manages a shopping cart using lists. It should allow the user to:

# Add items with quantity and price

# Remove items

# Update quantities

# Show total bill

# Apply discounts if certain conditions are met
my_cart=[]
category=[["apples","oranges","mangoes","peach"],["tomato","onion","cucumber","garlic"],["pepsi","fanta","dew","sevenup"]]
print("\033[1mWELCOME TO DARAZ ONLINE SHOPPING\033[0m\nCATEGORIES::- FRUITS , VEGETABLES , COLD DRINKS ")
ask=input("PLEASE WRITE  THE CATEGORY OF ITEMS YOU WANT TO BUY OR ADD TO CART::- ")
if ask=="fruits" or ask=="fruit":
 print("-:\033[1mWe HAVE FOLLOWING FRUITS\033[0m:-")
 for items in category[0]:
    print(items.upper(),end=", ")
 ask2=input("\nWHICH FRUIT WOULD YOU LIKE TO BUY ::- ")
 ask3=int(input("PLEASE TELL US QUANTITY OF FRUITS::- "))
 if ask2=="apples"or ask2=="oranges"or ask2=="mangoes"or ask2=="peach":
   for i in range(ask3):
    my_cart.append(ask2)
 print(f"{ask3} {ask2} are added to your cart ::- {my_cart}")    
elif ask=="vegetable" or ask=="vegetables":
 print("-:\033[1mWe HAVE FOLLOWING VEGETABLES\033[0m:-")
 for items in category[1]:
   print(items.upper(),end=", ")
 ask2=input("\nWHICH VEGETABLE WOULD YOU LIKE TO BUY ::- ")
 ask3=int(input("PLEASE TELL US QUANTITY OF VEGETABLES::- "))
 if ask2=="tomato"or ask2=="cucumber"or ask2=="onion"or ask2=="garlic":
    for i in range(ask3):
     my_cart.append(ask2)
 print(f"{ask3} {ask2} are added to your cart ::- {my_cart}")    
elif ask=="colddrinks" or ask=="cold drinks" or ask=="cold drink"or ask=="colddrink":
 print("-:\033[1mWe HAVE FOLLOWING COLD DRINKS\033[0m:-")
 for items in category[2]:
   print(items.upper(),end=", ")
 ask2=input("WHICH COLD DRINK WOULD YOU LIKE TO BUY ::- ")
 ask3=int(input("PLEASE TELL US QUANTITY OF COLD DRINK::- "))
 if ask2=="pepsi"or ask2=="sevenup"or ask2=="fanta"or ask=="dew":
    for i in range(ask3):
     my_cart.append(ask2)
 print(f"{ask3} {ask2} are added to your cart ::- {my_cart}")     
 
