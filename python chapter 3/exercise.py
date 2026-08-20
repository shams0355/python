accounts=["yasir","ali","mehdi","musa","ali","muhamamd","wali","katib"]
print(accounts.index("musa"))#it prints the index of that element
accounts.pop()#by default deletes the last element of the lsit if nothing mentioned in between the braces
print(accounts)
print(accounts.count("ali"))
print(accounts.index("ali",1+1))#to print the index number of the second item in that lsit
accounts2=["sageer","esa","saleem"]
accounts.extend(accounts2)#it will two lsits
print(accounts)