# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myfile.txt','w')

# Get info 
print('Name',myFile.name)
print('Is  closed',myFile.closed)
print('Opening Mode',myFile.mode)

# Write to file
myFile.write('I love python ')
myFile.close()

# Append to file
myFile = open('myfile.txt','a')
myFile.write(' I also like machine learing')
myFile.close()

# Read from file
myFile =open('myfile.txt','r+')
text = myFile.read(100)
print(text)