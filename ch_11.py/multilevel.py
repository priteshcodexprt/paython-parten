class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")
class Employee(Person):
    company="Honda"


    def getSalary(self):
        print(f"The salary is {self.salary}")
    def takeBreath(self):
        print(" i am an Employee so lucky breathing ..")

class programmer(Employee):
    company="Fiver"
    def getSalary(self):
        print("No salary for programmer!")
p=Person()
p.takeBreath()
e=Employee()
print(e.company)
e.takeBreath()
pr=programmer()
print(pr.company)
print(p.country)