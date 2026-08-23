your_set={4,5,3,2,6}
my_set={3,4,6}
#for union of the two sets
print(your_set.union(my_set))
#for intersections 
print("this is the intersection of the two sets which we have given to the system at earlier",your_set.intersection(my_set) )
print(my_set.issubset(your_set) )
print(your_set.issuperset(my_set))
#for difference purpose of two sets
print(your_set.difference(my_set))