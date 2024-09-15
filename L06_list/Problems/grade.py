grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

total =0

for grade in grades:
    total+=grade

print('Average is : ',total/len(grades))

""" 
list_01 =[]
n=int(input('Enter a value: '))
for i in range(n):
    value=int(input(f"Enter value for index {i}  "))
    list_01.append(value)
    
print(list_01) """

def square(a):
    return(a*a)

z=square
print(z(5))


# lst cmpr

list_5=[item for item in range(1,10)if item%2==0]

print(list_5)
list_06=[2, 4, 6, 8]
list001=[]
for number in range(len(list_06)-1,-1,-1):
    
    list001.append(list_06[number]*2)
    
    
print(list001)
    
list_07=[2, 4, 6, 8,9]

reversed_list =[item*2 for item in reversed(list_07)]
print(reversed_list)



