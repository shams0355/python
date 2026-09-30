# a=[1,[1,2,[1,"s"],4],2,[2,3,4,5]]
# print(a[1][2][1]) 
import numpy as np
a=np.array(["pak","karachi","peshawar"])
print(a)

# o=[x*2 for x in range(1,11)]#ye hai shortcut dekho
# print(o)
a=np.delete(a, np.where(a == "pak"))
print(a)
p=np.array([1,2,3,4,5])#to create an array
print(p)
p=np.append(p,9)#to append an element in the array
print(p)
p=np.flip(p)#to reverse the array
print(p)
p=np.insert(p,3,int(4.6))#assume 4.6 is a float, it will be converted to int
print(p)
p=np.delete(p,3)#to remove an element from the array enetring the index of the element
print(p)
p=np.delete(p,np.where(p==1))#to remove an element from the array enetring the value of the element
print(p)
