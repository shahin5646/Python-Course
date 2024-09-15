""" def sum(num1,num2):
    print(num1 + num2)
    
sum(25,125) #FItotalME:

# TODO: More About Function 

def summation(number1,number2):
    if (type(number1) is not int or type(number2) is not int):
        return
    return number1 + number2

total=summation('a',50)
print(total)

 """

 
def multiple_items(*args):                       # *args means it returns a tuple
    print(args)
    print(type(args))
    
multiple_items('Fuad','Shahin','Faruk')


def multi_key_items(**kwargs):            #It returns a dictionaries
    print(kwargs)
    print(type(kwargs))
    
multi_key_items(first_name='Fuad',Last_Name='Hasan',gmail='fuad01@gmail.com')

def shahin():
    print('HW')
    
shahin()

print('Shahin')
