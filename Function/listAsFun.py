# Accessing All elements in List




def greet_Guests(names):
    for name in names:
        msg='Assalamualikum '+name.title()
        print(msg)
    

guests=['Shahin','Onik','Nabil','Tanmir','Fuad','Faruk','Jim']

greet_Guests(guests)