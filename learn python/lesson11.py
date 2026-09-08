"""
يطبع القائمة كاملة.
يطبع أول طالب.
يطبع آخر طالب.
يضيف طالب جديد باستخدام .append().
يحذف طالب باستخدام .remove().
يطبع عدد الطلاب باستخدام len().
"""

names = ["Ali", "Omar", "KAD","Ahmed","faly"]

for name in  names:
    print(name)

print (names[0])
print (names[-1])

new_student = input("Enter new student name to add: ")
names.append(new_student)

student_to_remove = input("Enter student name to remove: ")
names.remove(student_to_remove)

print (len(names))
