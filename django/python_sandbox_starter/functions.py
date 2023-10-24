# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

def sayHello(name='Tupe'):

    print('Hello ' +  name)

def getSum(num1,num2):
    totol = num1+num2
    return totol

a = getSum(12,45)
#print(a)
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSume = lambda num1,num2 : num1+num2
print(getSume(12,34))