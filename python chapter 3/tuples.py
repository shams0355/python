#lets make a tuple 
my_tuple=("sunday","monday","tuesday","wednesday","thrusday","friday","saturday")
print(len(my_tuple))
print(max(my_tuple))#prints the maximum of the tuple ,if it contains numbers than it will prints the max other wise if there were any string then it prints max by its alphabetic order
print(min(my_tuple))

print(my_tuple.count("sunday"))

print(my_tuple.index("saturday"))
#slicing in the tuples 
print(my_tuple[0:6])
#how to store a single item in the tuple
ask_tuple=(2,)#if we want to store only one item in the tuple then we have to write in such a way that it contains one comma after our first element
                   #concatination in tuples 
ask_otuple=ask_tuple+my_tuple                   
print(ask_otuple)
#to add the elements of two tuples also
ali=(1,3,4,5)
murtaza=(7,2,45,6)
result=tuple(a+b for a,b in zip(ali,murtaza))
print(result)