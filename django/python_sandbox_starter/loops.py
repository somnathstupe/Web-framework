# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = [ 'sachin','pratiksha','pratik']
# 'for i in people:
#     print(i)
#break out 
# for i in people:
#     print(i)
#     if i=='pratiksha':
#         break
# for i in people:
#     if i =='pratiksha':
#         continue
#     print(i) 
     
for i in range(len(people)):
    print('Current person is ',people[i])

# While loops execute a set of statements as long as a condition is true.
count = 0 
while count <=10 :
    print('Count',count)
    count+=1
    