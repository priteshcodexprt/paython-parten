class Employee:
    company="Camel"
    bonus=100
    salary=5000
    location="Delhi"
    def showDetail(self):
        print("The Employee is created")
    

class Programmer(Employee):
    company="Visa"
    salary=500
    bonus=100
    location="Rajkot"


    
    





e = Employee()
# print(e.totalsalary)
print(e.bonus)
e.changeonus(455)
print(e.bonus)


# pr=Programmer()

# print(pr)





