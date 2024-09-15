
""" class Travel : 
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    def prime_member(self,all_guests):
        guest_list =[]
        
        for guest in all_guests:
            if self.age>= 22:
                print()
        
         """




























# TAking All different input at once
my_list =list()
Person = int(input('Enter: '))

for i in range(Person):
    data =input("Name/Age/Gender:  ").split('/')
    my_list.append(data)
    
print(my_list)

print(my_list[0])