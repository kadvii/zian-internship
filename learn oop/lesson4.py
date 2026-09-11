class Employee:
    company_name = "CodeZone"
    number_of_employees = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.number_of_employees += 1

    def get_info(self):
        return (
            f"{self.name} works as {self.position} "
            f"at {Employee.company_name}, Salary: {self.salary}"
        )

    def increase_salary(self, amount):
        self.salary += amount
        return f"{self.name} salary increased to {self.salary}"


employee_1 = Employee("AHMED", "Backend Developer", 800)
employee_2 = Employee("MAX", "Designer", 600)

print(employee_1.get_info())
print(employee_2.get_info())

print(employee_1.increase_salary(200))
print(employee_1.get_info())

print("Number of employees:", Employee.number_of_employees)