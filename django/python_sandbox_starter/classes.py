# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
# Create class 

class User:
    #Constructor
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age+=1


# Init User object
brad = User('Sominath','somnathtupe',25)
brad.name = 'Sachin'
brad.has_birthday()
print(brad.greeting())

#print(brad.name)

class customer(User):
     def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        self.balance=0


     def greeting(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance}'
     def set_balance(self,balance):
        self.balance=balance


    # Init cutomer 
ram = customer('ram','test@gmail.com',34)
print(ram.name)
ram.set_balance(500)
print(ram.balance)
print(ram.greeting())