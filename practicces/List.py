
reguler_user=[]

user_Number = int(input('Enter Number Of User: '))

for user in range(1,user_Number+1):
    users=int(input(f"User {user}: "))
    reguler_user.append(users)
    
print(reguler_user)

def sum_list():
    price=sum(reguler_user)
    print(price)
    
    
sum_list()