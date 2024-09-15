
# Tuple immutable Data Type but we can change value by converting it as a list then again convert into Tuples using Constructors

mytuple= tuple(('shahin',12,'fuad','shahin'))
anotherTuple=('buddy','roomie')

list_tpl =list(mytuple) #Converting AS a List
list_tpl.append('Bangladesh')

new_Tuples=tuple(list_tpl)
print(new_Tuples.count('shahin'))
print(new_Tuples.index("Bangladesh"))