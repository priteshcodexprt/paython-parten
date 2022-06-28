


from typing_extensions import Self


class programmer:
    Company="Goggle"
    def showDetail(self):
            print(f"This name is {self.Company}")

class Employee(programmer):
    Company="Visa"
    def getCompany(self):
        print(input("Enter your company name :"))

    
e=Employee()
p=programmer()
p.showDetail()
e.getCompany()
print(p.Company) 