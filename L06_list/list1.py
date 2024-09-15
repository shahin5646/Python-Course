
user =['shahin','onik','fayes',32,45]
emptylist =[]
print(user[0])
print(user[0:])
print(user[-3:-1])
print(len(user))

print('shahin'in user)

print(user.index(32))

print(user.index('fayes'))
print(45 in user)

# ________________________ADDDING ITEM ON LIST_______________________________________

user.append('Dave')
print(user)
user += ['shakib','tamim'] #it has to be list ,jodi list na hy tobe prottek item ekta ekta word kore list a add korbe
print(user)

user.extend(['Maxwell','starc'])
print(user)

emptylist.extend(user)
print('\n\n new list>=',emptylist)
print('---------------------------------------------')
print('Before Inserting 😐=',user)
user.insert(0,'texaaas')
print(user)
print('\n\n\n')
user.insert(6,'Dhaka_City')
print(user)

user[0:0]=['Shahin']
#___________NOT REPLACING THE VALUE OF THE DATA IN THAT POSITION____________________
print(user)

print('---------------------------------------------')
user[2:3]=['Bangladesh']
print(user)

print('\n\n\n\n---------------------------------------------')

# ________________________________REMOVING/DELETING FROM LIST_____________________________________

user.remove('fayes')
print('After Removing---->',user)

print(user.pop())
print(user)

del user[0:2]
print("Afterghfj",user)

# del emptylist
# print(emptylist)  it delete the list it shows not defined

print("______________________________________________________")
print(emptylist)
emptylist.clear()
print(emptylist)
#___________________SORTING________________________________________

list2 =[45,5,56,67,55,356]
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)
list2.reverse()
print(list2)

list3=['shahin','Ahammed','onik']
list3.sort(key=str.lower)
print(list3)

print(sorted(list3,reverse=True))

# __________________________COPYING STRING_________________________________

mylist2 =list2.copy()
mylist3= list(list3)
mylist4=list3[:]

