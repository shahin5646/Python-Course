# Creating An App Login 

class App:
    
    def __init__(self,users,storage,username):
        self.users = users
        self.storage = storage
        self.username = username
        
    def login(self):
        if self.username=='shahin' and self.users>1:
            print(f'Welcome {self.username}')
            print(f'Your storage size is  {self.storage}')
            
        elif self.users<=1:
            print(f"{self.users} is a invalid users amount.")
        
        else:
            print(f"{self.username} is a invalid name. ")
            
            
    def increase_capacity(self,user_storage):
        self.storage += user_storage
        
        return self.storage
    
users_amount =int(input("Enter User's Number :"))
users_storage =int(input("Enter User's Storage :"))
users_name = input('Enter username: ')
product_one =App(users_amount,users_storage,users_name)
product_one.login()
New_Stroage=print(f'Your increased Storage is : {product_one.increase_capacity(100)}')
            
        
