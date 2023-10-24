# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# person = { 
#     'first_name': 'Sominath',
#     'last_name': 'Tupe',
#     'age': 25
# }

#print(person)

# Using constructor 

person = dict(
    first_name ='Sominath',
    last_name='Tupe',
    age=25
)

print(person['first_name'])
print(person.get('last_name'))
print(person)

# Add key value
person['Phone'] = 1233
print(person.keys())
print(person.items())
print(person)

# List of dictionary

people = [
    {'name':'pratik','age':14},
    {'name':'pratiksha','age':18}
]

print(people)