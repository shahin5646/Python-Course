

class Online_Course:
    def __init__(self,instructor,course_name):
        self.instructor = instructor
        self.course_name = course_name
        self.students = []
        
    def enrolled_students(self,name):
        self.students.append(name)
        print(f"{name} has been enrolled in this Course!!!")
        
    def course_details(self):
        print(f"Course Name : {self.course_name}")
        print(f"Instructor Name : {self.instructor}")
        print(f"Enrolled Students:{','.join(self.students)} ")   #TODO
        
    def completed_course(self,name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} student has been completed the course.")
            
        else:
            print(f'{name} does not enrolled the course!!!')
            
    def avg_grade(self,grades):
        total = sum(grades)
        average = total /len(grades)
        print(f'Average grade: {average}')
        
        
course_input = input('Enter Course Name: ').title()
instructor_name   = input('Enter Instructor Name: ').title()
student = input('Enter student Name : ')
grades =[90,80,56,85,92,55]

course = Online_Course(instructor_name,course_input)
course.avg_grade(grades)
course.enrolled_students(student)
course.course_details()
course.completed_course(name='Shahin')  #TODO completed_course(name) same variable name






