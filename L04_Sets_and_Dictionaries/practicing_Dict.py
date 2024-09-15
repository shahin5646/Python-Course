import sys

users ={
    "name":'fuad',
    'pass':'diu_student',
    'Motive of Living':'Watching Hentai'
}
user2=dict(name='tanmir', password='qwersd')
# print(users)
# print(user2)
# print(type(user2))

# _________Accessing Items_________

print(users['pass'])
print(user2.get('password'))

# _________list all Items_____

print(user2.keys())
print('\n\n____________________________________')
print(users.values())

print('\n\n____________________________________')
print(user2.items())

print('pass' in users)
print('\n\n____________________________________')
print('pass' in user2)

# ____________Adding Items________________

user2['password'] ='tanmmirKhan123@'
print('\n\n____________________________________')
print(user2)

user2.update({
    'home':'Uttora',
    'Education':'DIU',
    'Travel':'Bus'
})
user8={
    'Status':'Single',
    'Class':'302'
}
user2.update(user8)

print('\n\n____________________________________')
print(user2)

# __________removing and Deleting Items________________

print('\n\n________________After Update____________________')

print(user2.pop('Education'))
print(user2)
print('\n\n________________After Update____________________')

print(user2.popitem())

del users['pass']
print(users)

users.clear()
print(users)
print('\n\n________________😁😁😁After Update😁😁😁____________________')
# del users
print(users)

# _____________________Copy________________

user3=user2.copy()
print(user2)
user3.update({'Hoby':'Scrolling Facebook','Strength':'Integrity'})
print('\n\n________________After Update____________________')
print(user3)

user4=dict(user3)
print('\n\n________________After Update____________________')
print(user4)

# Not copy
user5 =user4
print('\n\n________________After Update____________________')
print(user5)
print('\n\n________________Before  Update____________________')
print(user4)
user5.update({'Programming Skills':'Intermediate','Favourite Game':'PUBG'})
print('\n\n________________After  Update____________________')
print(user4)
# ___________Nested Dictionaries________________

CSE_Department={
    'Student_name':'Shahin',
    'Student_ID':'221-15-5646',
    'favourite_Language':'Python'
}

BBA_Student={
    'Student_Name':'Fayes Farhan',
    'Student_ID':'221-15-',
    'favorite_language':'English'
}

DIU_Student={
    'Department_01':CSE_Department,
    'Department_02':BBA_Student,
    'Batch':'221'
}

print(DIU_Student['Department_01']['Student_name'])

print(DIU_Student['Department_02']['Student_ID'])
