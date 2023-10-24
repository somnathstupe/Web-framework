# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "sachin"
age = 20
#concatnate 
#print("Hello "+name + 'and age'+ str(age))

# String Formatting

#Argument by position 
#print(' {1},{2},{0}'.format('a','b','c')) 

#Argument by name 
#print('My name is {name} and I am {age} '.format(name=name,age=age))

# F-string (only in 3.6+)
print(f"my name is {name} I an age{age}")

# String Methods

s = 'hello there world '

# Capitalise first letter

print(s.upper())
print(s.swapcase())
sub = 'l'
print(s.count(sub))