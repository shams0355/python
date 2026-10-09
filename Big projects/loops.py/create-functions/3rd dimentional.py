import numpy as np
new=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(new,type(new),new.ndim)

if new[0,0,1]==2:# first is block no, second is row no, and the third is the column no
    print(new[0,0,1])
    print("yes you are right")
print(new.shape)    

#to create multi-dimentional array
hot=np.array([1,2,3],ndmin=12)
print(hot.ndim)