""" dictu_1={
    'm':25,
    'n':30,
}
total_marks=0

for v in dictu_1.values():
    total_marks= total_marks + v
    
print(total_marks) """

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