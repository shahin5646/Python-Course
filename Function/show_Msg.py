""" Message: Write a function called display_message() that prints one sen- tence telling everyone what you are learning about in this chapter . Call the function, and make sure the message displays correctly .
"""

def display_message():
    print('what you are learning about in this chapter?')
    

display_message()

""" Favorite Book: Write a function called favorite_book() that accepts one parameter, title . The function should print a message, such as One of my favorite books is Alice in Wonderland . Call the function, making sure to include a book title as an argument in the function call . """

def favorite_book(bookname):
    print("One of my favourite book is "+bookname.title()+'.')
    
favorite_book('Alice in Wonderland')



def describe_pet(animal_type, pet_name):
    print('\n\nI have a '+animal_type+'.')
    print('My '+animal_type+"'s name is "+pet_name.title())
    
describe_pet('hamster', 'harry')