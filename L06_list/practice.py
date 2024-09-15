import sys
classmates =['fuad','onik','faruk','tanmir']
numbers=[12,52,354,66,6,3]
print(classmates.index('onik'))
print(classmates[-3:-1])
print(len(numbers))

print('fuad' in classmates)
# ______________Adding Value________________
numbers.append(565)
print(numbers)
classmates.extend(['shahin','prince'])
print(classmates)
classmates += ['Tanbir','Nabil']
print(classmates)
emptylist=[]
emptylist.extend(classmates)
print('\n\n New Value after changing: ',emptylist)
emptylist.insert(0,'Shahin Ahmed')
print(emptylist)

emptylist[3:3]=[565]
print(emptylist)

emptylist[-3:-1] =['Welcome1233']
print("\n\n\n The new List= ",emptylist)

# __________________Removing/deleting___________________
emptylist.remove('Welcome1233')
print(emptylist)
print('\n\n\n\n\n')

del emptylist[0:4]
print(emptylist)

print(emptylist.pop())
# del emptylist
# print(emptylist)
print('\n\n\n\n\n')
emptylist.clear()
print(emptylist)

# _____________sorting_______________
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers.reverse()
print(numbers)
classmates.sort(key=str.lower)
print(classmates)
classmates.reverse()
print(classmates)

print(sorted(numbers,reverse=True))


# ________________copy_____________
newlist=numbers.copy()
print('\n\n\n\n\n')
anotherList =newlist[:]
newL =list(newlist)
print(newL)