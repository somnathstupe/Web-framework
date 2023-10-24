# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json 

#Sample JSON 

userJSON = '{"first_name":"sominath","last_name":"Tupe","age":25}'

#Parse to dict

user = json.loads(userJSON)

print(user) 
print(user['first_name'])

# Parse dict to json

car = {'make':'ford','model':'Mustang','year':1997}

carJSON = json.dumps(car)
print(carJSON)