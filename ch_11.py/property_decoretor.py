class Employee :
    company="Bharat Gas"
    salary=5800
    salarybonus=500
    # totalsalary=6300

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.totalsalary = val - self.salary


e=Employee

e.totalsalary = 9000
print(e.totalsalary)
# print(e.salary)
print(e.salarybonus)

    