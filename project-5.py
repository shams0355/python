l=1
o=2
# # lets swipe both variable values
l,o=o,l
print("l's value is ",l,"\no's value is ",o)
#lets try it for three vaiables values
k=3
g=4
f=5
# #lets swipe these three variables values
k,g,f=f,g,k
print("k's value is ",k,"\ng's value is ",g,"\nf's value is ",f)
#lets do this by another way
a=1
b=2
c=3
d=4
print("Before swaping their origional vlaues was these a, b, c, d, respectively",a,b,c,d)
temp_a=a
temp_a=d
temp_b=b
temp_b=c
c=b
d=a
#After swaping values
print("After swaping their values are these a, b, c, d, again respectively",temp_a,temp_b,c,d)