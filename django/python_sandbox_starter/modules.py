# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Core 
import datetime 
from datetime import date 
import time
from time import time

# Pip module 
import camelcase

#today = datetime.date.today()
today = date.today()

camel = camelcase.CamelCase()
text = 'hello there is world'
print(camel.hump(text))



#timestamp = time.time()
timestamp = time()
print(timestamp)

print(today)


# Custom module
import validator
from validator import validate_email

email = 'test@test.com'

if validator.validate_email(email):
    print('Email is valid')

else:
    print("not email")