class Employee:
    company="CodexPrt"
    Level=0
    def upgradeLevel(self):
        self.Level=self.Level+1
        
class BaseData:
    company="Visa"
    eCode=150


class programmer(Employee,BaseData):
    name="Harry"


p=programmer()
# p.upgradeLevel()
print(p.company)
