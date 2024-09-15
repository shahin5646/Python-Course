# marks and subject
""" 
marks ={}

subject_count =int(input('How many Subject: '))

for i in range(0,subject_count):
    subject_name=input(f"Enter Subject name:")
    subject_marks=int(input(f"Enter marks of {subject_name}="))
    marks[subject_name]=subject_marks
    
print(marks)
 """
# convert two list into a dictionary

list_01=[1,2,3,4,5,6,7]
list_02=['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
dictionary={}
""" def insert_dict():
    for i in range(0,len(list_01)):
        dictionary[list_01[i]]=list_02[i]
        
    print(dictionary)
    
insert_dict() """

for i in range(0,len(list_01)):
        dictionary[list_01[i]]=list_02[i]
        
print(dictionary)
    