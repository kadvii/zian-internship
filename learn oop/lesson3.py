# تاسكك الأول المعدّل
# كمّل نفس كلاس Student وأضف داخله Method اسمها:
# get_info()
# ترجع نصاً بهذا الشكل:
# Name: AHMED, Age: 40, Courses: ['CS']
# وأضف Method ثانية:
# increase_age()
# تزيد عمر الطالب سنة واحدة.
# المطلوب بالتجربة:
# student_1 = Student("AHMED", 40, ["CS"])
# student_2 = Student("MAX")

class student:
    number_of_student = 0
    def __init__(self,name,age = 0 ,courses = "none"):
        self.name = name
        self.age = age
        self.courses = courses
        student.number_of_student+= 1

    def get_info(self):
        return f"name: {self.name}, Age: {self.age}, Courses: {self.courses}"

    def inscrease_age(self):
        self.age += 1
        return self.age
    
student_1 = student("AHMED" , 40 , ["CS"])
student_2 = student("MAX")

print(student_1) 
print(student_2) 

print("Number of students:", student.number_of_student)