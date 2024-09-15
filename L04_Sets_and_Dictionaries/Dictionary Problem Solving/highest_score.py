""" 
Store name as a Key, and 5 marks in a List as a value in dictionary.
Store details of at least 5 students. Print the name of the student who got
highest marks.
"""

students_data ={
    " Studentl " :[85,90,96,94,89],
    " Student2 " :[56,85,64,56,86],
    " Student3 " :[36,85,89,56,67],
    " Student4" :[56,85,64,68,80],
    " Student5 " :[90,68,45,95,48]
    }   

highest=0
name_student =''

for name,marks in students_data.items():
    total=sum(marks)
    if total>highest:
        highest=total
        name_student=name
        print(f"{name_student} got highest marks of {highest}")

 