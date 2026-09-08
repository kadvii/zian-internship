"""
Do you have a student ID? yes/no
"""


student = (input("Do you have a student ID ? yes/no"))

is_student = student == "yes"



if is_student:
    print("You are a student")
else:
    print("You are not a student")