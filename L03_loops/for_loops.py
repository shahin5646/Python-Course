names=['Shahin','Fuad','Onik','Faruk']

""" for x in names:
    if x=='Onik':
        break
    print(x)
     """
# Continue stop the current iteration and iterate the loop
""" 
for x in names:
    if x=='Fuad':
        continue # It will skip Fuad and print other values
    print(x)
     """
"""      
for x in range(1,11):
    print('5 * {} = '.format(x),5*x)


 """
 
# for c in range(10,100,10):
#     print(c)
  
names=['Shahin','Fuad','Onik','Faruk']  
actions=['Codes','Sleeps','Eats']

""" for name in names:
    for action in actions:
        print(name+ ' '+action+'.')

print('\n\n')

for action in actions:
    for name in names:
        print(name+' '+action+'.') """
        
        

for i in range(1,6):
    for j in range(1,6):
        print('*',end=' ')
    print()