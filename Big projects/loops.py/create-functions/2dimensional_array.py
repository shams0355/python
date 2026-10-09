import numpy as np
nw=np.array([[1,2,3],[4,5,6],[7,8,9]])#it will make a matrix 
print(nw)
print(nw[2,2])#address of the value interms of row by column
nw=np.delete(nw,2,axis=0)
nw=np.insert(nw,2,[89,23,34],axis=0)#axis=0 means row and axis=1 means column
print(nw)