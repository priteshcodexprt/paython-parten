class Employee:
    company="Goggle"
    def showDetails(self):
        print("The is on Employee")

class Programmer(Employee):
    Language="python"

    def getLanguage(self):
        print(f"the language is {self.Language}")
e=Employee()
e.showDetails()
p=Programmer()  