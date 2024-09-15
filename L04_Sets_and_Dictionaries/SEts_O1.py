# Practicing Sets In Python

set_01={1,2,5,6,7,8}
set_02={9,10,11,12}
set_00={9, 10, 11, 12, 565,5745,54,3535,345}
print(set_01)
print(type(set_02))
print(len(set_02))

set_03={True,1,3,2,6,False,4,9,8}
print(set_03)
set_03.union(set_01)
print(set_03) #print in a sorted way

# ________Adding Items______

set_03.pop()
print(set_03)
set_03.pop()
print(set_03)

set_03.add(565)
print(set_03)

set_03.update(set_02)
print(set_03)

set_03.intersection_update(set_00)
print(set_03)

print('\n________________________________')
set_02.intersection_update(set_00)
print(set_02)

set_02.intersection(set_03)
print(set_02)

set_02.symmetric_difference_update(set_03)
print(set_02)