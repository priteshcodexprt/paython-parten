class Employee:
    company="Goggle"
harry=Employee()
rajani=Employee()
print(harry.company)
print(rajani.company)
Employee.company="Youtube"
print(harry.company)
print(rajani.company)
harry.salary=300
rajani.salary=500
print(harry.salary)
print(rajani.salary)