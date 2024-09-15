""" 
Store "name" of a student as Key, "list of 5 marks" of that student as
a Value. Store at least 5 student names. Print the sum and percentage of all
the students.

"""

students_data ={
    " Studentl " :[85,90,96,94,89],
    " Student2 " :[56,85,64,56,86],
    " Student3 " :[36,85,89,56,67],
    " Student4" :[56,85,64,68,80],
    " Student5 " :[90,68,45,95,48]
    }   


for name,marks in students_data.items():
    total=sum(marks)
    percentage =(total/500)*100
    print(f"{name} has got total {total} and his percentage is {percentage:.2f}",end='\n')