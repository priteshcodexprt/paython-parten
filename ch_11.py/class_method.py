class Employee:
    company="Camel"
    Salary=100
    # location="Rajkot"
    

    @classmethod
    def ChangeSalary(cls,Sal):
        cls.ChangeSalary=Sal

E=Employee()
print(E.Salary)
E.ChangeSalary(455)