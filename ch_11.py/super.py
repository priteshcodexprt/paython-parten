class Person:
    country = "India"


    def takeBreath(self):
      
        print("I am breathing...")

        
    def __init__(self) :
        super().__init__
        print("Initializing person...\n")

class Employee(Person):
    company="Honda"
     
    def __init__(self) :
        super().__init__
        print("Initializing Employee..\n")
   
    def getSalary(self):
        print(f"The salary is {self.salary}")

    
    def takeBreath(self):
        super().takeBreath()
        print(" i am an Employee so lucky breathing ..")


class programmer(Employee):
    company="Fiver"

    def __init__(self) :
        super().__init__
        print("Initializing Programmer..\n")


    def getSalary(self):
        print("No salary for programmer!")





# p=Person()
# p.takeBreath()
e=Employee()
# print(e.company)
# e.takeBreath()
# pr=programmer()
# print(pr.company)
# print(p.country)