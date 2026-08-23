#to make an empty set we use this
mt_set=set()
print(type(mt_set))
#To add elements into existing set
mt_set.add(1)
#To make a shallow copy of set 
new_set=mt_set.copy()
#To clear the set
new_set.clear()
print(new_set)
#to print items in the set
print(mt_set)
#to print only elements
for item in mt_set:
    print(item)
#to remove any element
mt_set.discard(1)   
print(mt_set)