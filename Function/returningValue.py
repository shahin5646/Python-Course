


def name_of_User(first_name,last_name):
    full_name=first_name +' '+last_name
    return full_name.title()

user_full_name=name_of_User('Shahin','Miah')

print(user_full_name)


# Create an Optional variable

def User_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        fullname=first_name+' '+middle_name+' '+last_name
        
    else:
        fullname=first_name+' '+last_name
    return fullname

cricketer=User_formatted_name('Travis','Head')

print(cricketer)

cricketer=User_formatted_name('Sachin','Tendulkar','Ramesh')
print(cricketer)