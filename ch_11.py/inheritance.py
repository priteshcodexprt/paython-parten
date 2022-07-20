class Employee:
    company="Goggle"
    def showDetails(self):
        print("The is on Employee")

class Programmer(Employee):
    Language="python"
    Datatype="Javascript"

    def getLanguage(self):
        print(f"the language is {self.Language}")
        print(f"the language is {self.Datatype}")
e=Employee()
e.showDetails()
p=Programmer()
p.getLanguage()
p.Datatype()