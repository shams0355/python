o=[[1,2],[2,3],[4,5]]
print(o[0][1])#it will print 2
#to add any item in nested lsit
o.insert(1,2)#to insert any item while push the next element to one right side
print(o)
o[0][1]=5#add element in that specific nested lsit
print(o)
#to insert any element in the specific nested lsit
o[2].insert(2,90)
print(o)
#to add items in list using loop
h=[]
for i in range(3):
    h.append("mango")
print(h)

#slicing in the lists
e=[1,2,3,4,5,5,6]
print(e[0:3])
#print maximum or minimum in the lists
print(max(e))
print(min(e))
#to add two lists by adding also thier respective elements
f=[1,3,4,5,5,6]
solve=list(a+b for a,b in zip(e,f))
print(solve)