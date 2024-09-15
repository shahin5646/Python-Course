# Checking Values Exist or not & Changing it

def check_ifExist(key,dictionaries):
    if key in dictionaries.keys():
        print('Key Exists')
        dictionaries.update({'key':'Changed'})
    else:
        print('Key Does not Exist😒')



dictionaries={'Name':'Shahin','Favorite_Book':'Steal Like an Artist','University':'Daffodil'}
key='Favorite_Book'
check_ifExist(key,dictionaries)

print(dictionaries)