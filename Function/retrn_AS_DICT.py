
# With an Optional Parameter age
def user_info(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    
    if age:
        person['age']=age        # Creating a new key in the existed dictionaries
    return person

person_name=user_info('Shahin','Ahmed',20)

print(person_name)

person_name=user_info('Shahin','Ahmed')

print(person_name)