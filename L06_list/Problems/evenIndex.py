# Even numbers print



list_01 =[1,30,40,66,78,68,9,678,56]

for i in range(0,len(list_01)):
    if i%2==0:
        print(list_01[i],end=' ')
        
        
# count even numbers in a list
count =0
for i in list_01:
    if i%2==0:
        count+=1
        
        
print('\n total Even number: ',count)

# How many numbers divisible by 2 & 5
flag =0
for i in list_01:
    if i%2==0 and i%5==0:
        flag=flag+1

print('\n numbers are: ',flag)

# Sum of all even Numbers in a list
list_02=[10,19,20,30,29,100,150,4,400]
sum =0
for i in list_02:
    if i%2==0:
        sum =sum+i

print('Total =',sum)

# LArgest number in a list

largest =0

for i in list_02:
    if i>largest:
        largest=i
        
print('The largest Number:',largest)

# Taking user Input

list_03=[]
for i in range(5):
    value =int(input(f"enter a value for index {i}="))
    list_03.append(value)
    
print(list_03)