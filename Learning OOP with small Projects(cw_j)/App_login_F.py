# App Login


class App:
    def __init__(self,user,storage,username):
        self.user=user
        self.username=username
        self.storage=storage
        
    def login(self):
        if self.username=='shahin':
            print(f'Welcome {self.username}')
            
        else:
            print(f'Enter The Correct Username!!')
            
    def increase_capacity(self,amount_increase):
        self.storage += amount_increase
        print(f"Storage updated!!!!")
        
    def check_upgrade(self):
        if self.storage<= self.user:
            upgrade_amt =int(input("Enter Amount to Upgrade: "))
            self.storage += upgrade_amt
            print('Updated your Storage !!!')
            
        else:
            print('You have ',(self.storage-self.user),' space in your storage')
            
            
user_one = App(25,35,'shahin')

user_one.login()
user_one.check_upgrade( )
        
user_one.increase_capacity(25)
user_one.check_upgrade()
user_two = App(25,12,'shahin')
user_two.check_upgrade()

user_two.check_upgrade()

