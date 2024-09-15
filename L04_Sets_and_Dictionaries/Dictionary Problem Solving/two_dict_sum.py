""" dl = {'a': 100, 'b': 200,'c':400}
d2={'a': 300, 'b': 200, 'd':500}

# Output
{'a': 400, 'b': 400, 'c': 400, 'd': 500}
"""

d1 = {'a': 100, 'b': 200,'c':400}
d2={'a': 300, 'b': 200, 'd':500}
result={}

for k,v in d1.items():
    result[k]=v
    
    
for k,v in d2.items():
    if k in result:
        result[k]=result[k]+v
    else:
        result[k]=v
        
print(result)