import numpy as np
my_array=np.array([])
ask=int(input("enter how many numbers do you want to enter in array::-  "))
seq=["1st","2nd","3rd","4th","5th","6th"]
for i in range (0,ask):
    value=int(input(f"enter your {seq[i]} number ::- ")) 
    my_array=np.append(my_array,value)
print(my_array,type(my_array))
print(my_array.ndim)
import random# random number list
new=[random.randint(1,30) for i in range(1,20)]
print(new)

