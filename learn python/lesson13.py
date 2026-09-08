"""
يطبع جميع الأسماء.
يطبع عدد الطلاب.
يطبع أول طالب.
يطبع آخر طالب.
"""
names = []
i = 0

while i < 5:
    name = input("enter the name: ")
    names.append(name)
    i += 1

print(len(names))
print(names[0])
print(names[-1])

for i in  names:
    print(i)
