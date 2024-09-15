# Updated Version Of Course Management System

class Online_Course:
    def __init__(self,instructor,course_name):
        self.instructor = instructor
        self.course_name = course_name
        self.students = []
        
    def enrolled_students(self,student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in this Course!!!")
        
    def course_details(self):
        print(f"Course Name : {self.course_name}")
        print(f"Instructor Name : {self.instructor}")
        print(f"Enrolled Students: ")   #TODO
        for student in self.students:
            print(student.name)
        
    def completed_course(self,name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
                print(f"{name} student has been completed the course.")
                   
        print(f'{name} does not enrolled the course!!!')
            
    def avg_grade(self,grades):
        total = sum(student.grades)
        average = total /len(student.grades)
        print(f'Average grade: {average}')
        

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
        
        
course_input = input('Enter Course Name: ').title()
instructor_name   = input('Enter Instructor Name: ').title()
course = Online_Course(instructor_name,course_input)

num_student =int(input('Enter Num of Students: '))

for _ in range(num_student):
    student_name = input('Enter a Student Name: ')
    grades =[]
    
    for _ in range(3):
        grade = int(input('Enter a grade: '))
        grades.append(grade)
        
    student =Student(student_name,grades)
    course.enrolled_students(student)
    course.avg_grade(student)
    
course.course_details()
course.completed_course('Fuad')
course.course_details()






