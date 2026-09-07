class student:
    number_of_student = 0
    def __init__(self,name,age = 0 ,courses = "none"):
        self.name = name
        self.age = age
        self.courses = courses
        student.number_of_student+= 1

student_1 = student("AHMED" , 40 , ["CS"])
student_2 = student("MAX")

print(student_1) 
print(student_2) 

print("Number of students:", student.number_of_student)