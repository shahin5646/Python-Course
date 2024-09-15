# Online Course Management

class Online_Course:
    def __init__(self,instructor,course_name):
        self.instructor = instructor
        self.course_name = course_name
        self.students =  []
        
    def enrolled_student(self,student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the Course")
        
    def course_details(self):
        print(f'Instructor name: {self.instructor}')
        print(f'Course name: {self.course_name}')
        print(f'Enrolled students: ')
        for student in self.students:
            print(f"{student.name}")
        
    def completed_course(self,name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
                print(f'{name} has been completed the course')
                
        print(f"{name} has not enrolled the course")
            
            
    def avg_grade(self,grades):
        total = sum(student.grades)
        average = total / len(student.grades)
        print(f"Average Grade: {average}")
        

class Student_Info:
    def __init__(self,name,grades):
        self.name = name 
        self.grades = grades
        
        
course_input = input("Enter the course name: ").title()
instructor = input('Enter the Instructor Name : ').title()

course = Online_Course(instructor,course_input)

num_students = int(input('Enter how many students want to Enroll : '))

for _ in range(num_students):
    student_name = input('Enter Student Name: ')
    grades = []
    
    for _ in range(3):
        grade = int(input("Enter your grades: "))
        grades.append(grade)
        
    student = Student_Info(student_name,grades)
    course.enrolled_student(student)
    course.avg_grade(student)
course.course_details()
print('\n____________________________')
course.completed_course(name='shahin')
course.course_details()
print('\n____________________________')
course.course_details()