# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruit_tuple = ('Apple','Orange','Mango')

# Get single value
#print(fruit_tuple[1])

# tuples with single value put comma

#s = ('Apple',)
#del s 
#print(s)


#print(fruit_tuple)
# A Set is a collection which is unordered and unindexed. No duplicate members.

fruit_set = { 'Orange','Mango','Apples'}
print(fruit_set)
print('Apples' in fruit_set)
fruit_set.add('grap')
print(fruit_set)
