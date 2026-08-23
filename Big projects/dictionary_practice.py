#lets make a dictionary to practice
my_dict={"ali":[12,13,14],#if we want to store multipe items in a dictionary then we have to make another list as a value of that key
         "muhammad":[16,17,15,19]
         }
print(my_dict)
print(my_dict["ali"][1])#it will print the value 13 cuz in the 1 index of list which is considered as a value of key(ali) so it will print that value exixts in that index
my_dict.update({"ali":[12,13,14,15]})#it will update the list values ,overwrites when some thing exists in that list or value or we use it if we want to add a new record
print(my_dict)
print(my_dict.keys())#it will print all the key values in that dictionary
print(my_dict.values())#it will print all the values correspondence to values
print(my_dict.get("muhammad")[2])#we use get() function cuz it doesn't shows error if it not finds the value
# #it will clear the dictionary ,makes the dictionary to seem as empty
# my_dict.clear()
# print(my_dict)
for key,values in my_dict.items():
    print(f"{key} has gained these marks across different subjects::- {values}")
print(my_dict.get("wali"," aisa koi nam hi nahi hai chutiye"))   
#to make a shallow copy of dictionary ,to use it without changing the origional dictionary
new_dictionary=my_dict.copy()
print(new_dictionary)
#to get the keys from another list
p=["ali","hamza","wali ur rehamn"]
print(p.pop())#pop fuction by default removes the last item which is added to the lsit or to a dictionary
o=dict.fromkeys(p,0)
print(o)
#to remove specific key and its corresponding value
print(my_dict.pop("hamza","ye kaha say aya chutiye"))
print(my_dict.items())
#remove by using LIFO mehtod 
#Means the last item which is added is first to be removed
print(my_dict.popitem())#the pop() function usually returns the value whish is to be removed by system, and it removes that item
print(my_dict)
print(len(my_dict))#it will print the length of the dictinary
