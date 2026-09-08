students = []

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        # إنشاء قاموس الطالب وإضافته للقائمة
        student = {"name": name, "age": age, "course": course}
        students.append(student)
        print(f"✓ Added {name} successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- All Students ---")
            for index, student in enumerate(students, 1):
                print(f"\nStudent #{index}:")
                for key, value in student.items():
                    print(f"  - {key}: {value}")

    elif choice == "3":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option, please try again.")