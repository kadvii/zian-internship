class student:
    def __init__(self, name, age=0, courses="none"):
        self.name = name
        self.age = age
        self.courses = courses

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


student_1 = student("AHMED", 40, ["CS"])
student_2 = student("MAX")

student_1.set_name("ALI")
print(student_1.get_name())