#Check if the value exist or not 



marks   ={
    'python':75,
    'accounting':80,
    'system':85
}

subject_name=input('Enter a subject:')

if subject_name in marks.keys():
    print(f"The marks of {subject_name}=",marks[subject_name])
    
else:
    print('Invalid')
    