from datetime import datetime


class Employee:
    company="Goggle"
    
    def getSalary(self):
        print(f"Salary for this employee working in {self.company}is {self.Salary}")
    @staticmethod
    def greet():
        print("Good morning ,sir")
    @staticmethod
    def time ():
        print("This time is 9 Am ")
harry=Employee()
harry.Salary=100000
harry.greet()
harry.time()