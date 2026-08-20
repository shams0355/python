# strings are immutable
#string slicing
ask="pakistan"
ask1=ask[0:7:3]#it will print PIA
print(ask1)
ask2=ask[0:5]
print(ask2)
a=1332434#integers doesn't have length
a=str(a)#so we simply converted the integer into string simply by using the technique called as type casting
print(len(a))
# To replace from any string
b="i have 3 apples and 7 oranges"
repl=b.replace("3","5")
print(repl)
memo=b.replace("have","don't have")
print(memo)