class person:
    def name(self,company,city,salary,otherSalary,country): 
        self.city=city
        self.company=company
        self.country=country
        self.otherSalary=otherSalary
        self.salary=salary
class Freelancer(person): 
    company="Visa"
    city="colombia"
    country="Rush"
    salary=5555
    otherSalary=88888

    def showDetails (self):
         print(f"This city name is : {self.city}\n")
         print(f"This company name is : {self.company}\n")
         print(f"This salary name is : {self.salary}\n")
         print(f"This  otherSalary name is : {self.otherSalary}\n")
         print(f"This country name is : {self.country}\n")

    @property
    def number (self):
        return self.salary + self.otherSalary



class programmer:
    language="python"

def language (self):
    print(f"programmer language is {self.language}")





p=person()

f=Freelancer()
f.showDetails()

pr=programmer
print(pr.language )

print(f.number)