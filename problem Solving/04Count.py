# Item in a list

def coun_items (list_01):
    count = 0
    for i in list_01:
        count+=1
    return count

list_items = ['mangoes','banba',12,65,6]
print(coun_items(list_items))