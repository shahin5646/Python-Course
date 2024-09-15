

def formatted_name(f_name,l_name):
    full_name =f_name +' '+l_name
    return full_name

while True:
    print('Enter your Name :')
    print('Enter q to exit anytime :')
    
    f_name=input('Enter Your First Name: ')
    if f_name == 'q':
        break
    
    l_name=input('Enter your last Name:')
    if l_name =='q':
        break

    user_name =formatted_name(f_name,l_name)

    print(user_name)

    
     
     
     
     
""" def get_formatted_name(first_name, last_name):
    
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
 """