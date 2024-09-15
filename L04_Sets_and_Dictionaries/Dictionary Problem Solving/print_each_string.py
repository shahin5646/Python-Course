""" 
Print each value as a dict
 sample I/O:enter a string: Hello Shahin
{'H': 1, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'S': 1, 'h': 2, 'a': 1, 'i': 1, 'n': 1} 

"""


my_string =input('enter a string: ')

frequency ={}

for i in my_string:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
        
print(frequency)