values={
    'book':'Atomic Habits',
    'song':'we will rock you',
    'degree':'CSE'
}
print(values)
print(type(values))

new_dict =dict(name='Shahin',id='221-15-5646')
print(new_dict)
print(len(values))

# _______Access Items__________
print(values.get('book'))
print(values['song'])

#___________Accessing/list all keys Keys______________
print(values.keys())

print(values.values())